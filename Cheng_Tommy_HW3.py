"""
@author: Tommy Cheng HW3
"""
"""
This program is a dataset plot function that plots different dataset into histogram, with the condition of discarding the 
outliers in the samples and finding the optimal binwidth of each histogram. A box-plot is also plotted for each variable.
I used freedman-diaconis rule for optimizing the binwidth and Interquartile 1.5 rule to sort out the outliers on the dataset
NOTE: The program will fail to plot some of the dataset with a lot of zero entries due to the calculate on Freedman-diaconis 
rules

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plot


'''
First import the dataset from the website and convert it to dataframe in python using pandas.
Then add the title to each column of the dataset
NOTE: for KDD data set, it is a zip file online and I have to download it manually to the local directory and work on it
'''
ab_cols = ['Sex', 'Length', 'Diameter', 'Height', 'WholeWt', 'ShuckedWt', 'VisceraWt', 'ShellWt', 'Rings']
abalone = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data", names = ab_cols)
diamonds = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/Ecdat/Diamond.csv', skiprows=1, names= ['carat', 'colour','clarity','certification', 'price'])
KDD = pd.read_csv("KDD.txt")



#extract the numerical columns from the dataset diamonds
carats = diamonds.ix[:,0]
price = diamonds.ix[:,4]


#separate out the set of the numerical column from the dataset abalone
length = abalone.ix[:,1]
diameter = abalone.ix[:,2]
height = abalone.ix[:,3]
wholeWt = abalone.ix[:,4]
shuckedWt = abalone.ix[:,5]
visceraWt = abalone.ix[:,6]
shellWt = abalone.ix[:,7]
rings = abalone.ix[:,8]


#Separate out the set of numerical columns from the dataset KDD using the data.frame.ix split function, the dataset is very unorganized and I'm not sure 
#Since the data set is very organized and undocumented, I just show 2 examples here 
col1 = KDD.ix[:,0]      #ages 
col4 = KDD.ix[:,3]




def optbinwith(n, a, b, iqr):
    '''
    This function calculates the optimal binwidth using freedman-diaconis rule
    Input: n = length of the columne (number of elements in the column)
    a = max value of the column 
    b = min value of the column
    iqr = interquartile range of the column
    Return: a float number, number of optimal bins
    '''
    
    h = 2 * iqr * n**(-1/3)
    ran = a - b
    bins = ran / h
    return bins




def split_dist(data):
    '''
    This function contains several procedures. First it finds the interquartile range of the data set 
    and use the dropna function to combine the subset of lower bound outliners, upper bound outliners and the core
    distribution. the IQR is recalculated again once the three boundaries are formed because there are 3 different 
    IQR in each set individually. The function will finally plots historgrams and box-plot 
    
    Input: a column of data
    Return: It plots histograms for the 3 separate sets and box-plot for the entire sets
    '''
    summary = data.describe()           #gives the descriptive stats
    q1 = summary['25%']                 #Q1 value
    q3 = summary['75%']         #Q3 value
    iqr = q3 - q1               #IQR
    lower_bound = q1 - 1.5 * iqr         #lower bound for IQR 1.5 rules 
    upper_bound = q3 + 1.5 * iqr          #upper bound for IQR 1.5 rules
    upper_outliers = data.where(data > upper_bound).dropna()     #extract upper bound
    lower_outliers = data.where(data < lower_bound).dropna()        #extract lower bound
    middle = data.where(data <= upper_bound).dropna()               #extract the core 
    middle = middle.where(middle >= lower_bound).dropna()           #extract the core
    
    
    if lower_outliers.size !=0:                     #check to see if the set is empty, if so , no plot
        summary2 = lower_outliers.describe()
        q11 = summary2['25%']                   #recalculates IQR
        q31 = summary2['75%']
        iqr2 = q31 - q11
        lowerbins = optbinwith(lower_outliers.size, float(lower_outliers.max()), float(lower_outliers.min()), float(iqr2))
        plot.figure()
        lower_outliers.plot.hist(bins= round(lowerbins)).set_title('Lowerbound outliers');
    if middle.size!= 0:                        #check to see if the set is empty, if so , no plot
        summary3 = middle.describe()
        q12 = summary3['25%']                   #recalculates IQR
        q32 = summary3['75%']
        iqr3 = q32 - q12
        midbins = optbinwith(float(middle.size), float(middle.max()), float(middle.min()), float(iqr3))
        plot.figure()
        middle.plot.hist(bins= round(midbins)).set_title('Core distribution')
    if upper_outliers.size !=0 :             #check to see if the set is empty, if so , no plot
        summary4 = upper_outliers.describe()
        q13 = summary4['25%']                #recalculates IQR
        q33 = summary4['75%']
        iqr4 = q33 - q13
        upperbins = optbinwith(upper_outliers.size, float(upper_outliers.max()), float(upper_outliers.min()), float(iqr4))
        plot.figure()
        upper_outliers.plot.hist(bins= round(upperbins)).set_title('Upperbound outliers')
    
    plot.figure()
    data.plot.box()             #plot box-plot for the entire set 



#Test case
split_dist(carats)
split_dist(price)
split_dist(length)
split_dist(col4)

'''comments: The Freedman-D rules does a pretty good job in picking the binwidth sizes and they show a clear distrituion for 
for most of the data. Also it fails to do so if the data set is too small. I.E : only a few outliers.
'''