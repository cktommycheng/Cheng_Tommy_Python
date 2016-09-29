#Stuart- As part of your documentation you should include the purpose (in the help format) and inputs to
#each of the major functions that you write (~one per problem). You have the information, just not as part of
#the functions themselves.
#Stuart- Any points lost due to lack of documentation or using script instead of functions
# can be regained if the issues are corrected. Please email me once you have corrected the issue
# and I will check your code.
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 15:31:15 2016

@author: Tommy Cheng HW1
"""


'''Problem 1: This function is a palindrome recogniser that accepts a file
name from the user, reads each line, and prints the line to the
screen if it is a palindrome.
'''
#Stuart- The problem asks for a function that takes a file name. So the entire
#problem should be wrapped by a function definition. Nice step to use only the lower case.

filename = input("Enter filename: ")    #ask for user input
file = open(filename)

#This defines a function to check to see if a word is palindrome, return true if it is"
def is_palindrome(text):
    revtext = text[::-1]
    if revtext == text:
        return True
#Stuart- You can use return on an expression for example
# return text==text[::-1]        

line = file.readline()          #read line
while line:
    templine = ''               #create storage variable
    lowcaseline = line;             
    lowcaseline = lowcaseline.lower()       #convert to lower case letter
    for i in range(len(lowcaseline)):   
        if ord(lowcaseline[i]) > 96 and ord(lowcaseline[i])<123:    #use ASCII code to check for lower case alphabets in the line
            templine = templine + lowcaseline[i]
        
    if is_palindrome(templine) == True:         #if it is true, print the line and indicators
        print(line + 'is a palindrome.')    
    else:
        print(line + 'is not a palindrome.')
        
    templine=''
    templine2=''
        
    line = file.readline()


file.close()


#-------------------------------------------------------------------------------------------------------------------------
"""
Created on Thu Sep 15 06:58:12 2016

@author: TommyCheng
"""
"""
Problem 2:  This program is a semordnilap
recogniser that accepts a file name 
from the user and finds and prints all pairs of words that are
semordnilaps to the screen. 
"""
#Stuart- The problem asks for a function that takes a file name. So the entire
#problem should be wrapped by a function definition. 

filename = input("Enter filename: ")        #prompt user for input
file = open(filename)

text = file.read().split()     #read the file and split the words into a list

semordnilap_list= []        #create a storage list

for word1 in text:          #nest for loop: 1st loop go through the wordbank
    for word2 in text:      #2nd loop goes through the wordbank again
        if word1 == word2[::-1]:    #check to see if the word is semordnilap 
            print(word1, word2)     #print words that are semordnilap
    
file.close()

#-------------------------------------------------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 13:40:14 2016

@author: Tshark
"""
"""
Problem 3: character frequency table
   Prompt ussers for a file name. And list the frequency of all the characters
"""


import string

def char_freq_table(name):

   file = open(filename)
   text = file.read()   #read file
   
   for i in range(len(string.printable)):       # For loop: Use str.count function to count the frequency
       print(string.printable[i],' ', text.count(string.printable[i]))  # of character 


filename = input("Enter filename: ")    #ask for user input

char_freq_table(filename)

#-------------------------------------------------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 12:54:36 2016

@author: Tshark
"""
'''
Problem 4 :This is a program speak_ICAO()able to translate any text (i.e. any string)
into spoken ICAO words with given pause time of words and letters
'''

import time
import os


#icao library
icao = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 
     'f':'foxtrot', 'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 
     'k':'kilo', 'l':'lima', 'm':'mike', 'n':'november', 'o':'oscar', 
     'p':'papa', 'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango', 
     'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee', 
     'z':'zulu'}

def speak_ICAO(text, pauseletter, pauseword):
    words = text.lower()
    words = words.split()     #make text lowercase and split the text into individual words)
    for word in words:
              
        for letter in word:      #nest for loop to check for the letters in 
            if letter in icao:          
                os.system("say " + icao[letter])
                time.sleep(pauseletter)
        time.sleep(pauseword)


speak_ICAO("Sup bro",2,1)

#-------------------------------------------------------------------------------------------------------------------------

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 06:58:47 2016

@author: TommyCheng
"""
'''
Problem 5: This function return all its hapaxes. Hapaxes are words which
occur only once in either the written record of a language, the
works of an author, or in a single text. 
'''

#Stuart- Again, it is best practice to write functions. This can greatly aid in 
#debugging.

import string

filename = input("Enter filename: ")
file = open(filename)
text = file.read().lower()

for pun in string.punctuation:          #get rid of punctuation by replacing it to "")
    text= text.replace(pun,"")
word_list = text.split()                #split the text into words only 
    
hapax = set()                   
repeat = set()          #count for duplicates

for word in word_list:
    if word not in hapax:           #add words if it is not in hapax
        hapax.add(word)
    else:
        repeat.add(word)        #add the repeated word in this list
    if word in repeat:          #remove the repeated words from hapaxes
        hapax.remove(word)
        
print('The hapaxes are: ')
for w in hapax:
    print(w)

#-------------------------------------------------------------------------------------------------------------------------

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 14:32:55 2016

@author: Tommy Cheng
"""
'''
    Problem 6: This program prompts user to enter a text file name, it will create a new text file in
    which all the lines from the original file are numbered from 1 to n
    (where n is the number of lines in the file).
'''

filename = input("Enter filename: ")    #ask for user input in the local directory 
file = open(filename)
line = file.readline() # read first line. This ensures proceeding loop runs at least once

i = 1            # assign iterator to number lines
    
 
new_text = ''       #create an empty str variable

while line:                     #loop through the line of the original file
    new_text += str(i) + ' '    #add the line number
    new_text += line            #add the line
    i += 1                      # add 1 to iterator
    line = file.readline()      #read the next line of the file
    
file.close()                    #closes the original file


new_filename = input('Enter a new file name: ')
new_file = open(new_filename, 'w')
new_file.write(new_text)
new_file.close()
    
#-------------------------------------------------------------------------------------------------------------------------

"""
Created on Thu Sep  8 19:23:11 2016

@author: Tommy Cheng
"""
'''Problem7
Write a program that will calculate the average word length of a text
stored in a file (i.e the sum of all the lengths of the word
the text, divided by the number of word ). 
'''


filename = input("Enter filename: ")
file = open(filename)

line = file.read()

text = line
text = text.lower() 
wordcount = 0           #set up the counter


for i in range(len(text)):
        if (ord(text[i]) > 96 and ord(text[i])<123 ):
            wordcount = wordcount +1     

#for i in range(len(text)):
#    if text[i] != ' ':
#        wordcount = wordcount + 1            

            
print(wordcount)

words = float( len(text.split()) * 1.0)

print ('The average word length of this text is: ', "%.1f"%(wordcount/words),'words' )

#-------------------------------------------------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 01:18:47 2016

@author: Tommy Cheng
"""

'''Problem 8 : Guess the number game: this program asks user to guess a number between
0 to 20 inclusively. The user has infintely many trials. When the user guesses it correctly,
it will 


'''

import random

num = random.randint(1, 20)     #generate a number between 1 to 0 inclusively
print(num)

print('Hello! What is your name?')
name = input('Enter your name: ')
print('\n',name,',', 'I am thinking of a number between 1 and 20. Take a guess.')

guess = 0           #initiate a varible
counter = 0         #counter

while guess!= num:
    guess = input('Your guess(integer): ')
    guess = int(guess)
    if guess < num:                     #if guess is lower than the answer, prompt user to enter again
        counter = counter + 1
        print('Your guess is too low. Take a guess')
    elif guess > num:                   #if guess is higher than the answer, prompt user to enter again
        counter = counter + 1
        print('Your guess is too high. Take a guess')
    elif guess == num:                  #if guess is right, end program and print our the total number of guesses
        counter = counter + 1
        print('Good job,',name,'! You guessed my number in', counter, 'guesses !')

#-------------------------------------------------------------------------------------------------------------------------

# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 01:38:28 2016

@author: Tommy Cheng
"""
'''
Problem 9 : This program is anagram game. It will generate an anagram from a random word in t
given list and prompt user to guess the word.
'''
import numpy
import random

color = ['orange', 'yellow', 'blue', 'red', 'brown', 'purple', 'green']        #word list
num = random.randint(0, len(color)-1)                       #generate a random color 
word = color[num]


def anagramgenerator(choice):
    order = numpy.random.choice(len(choice), len(choice), replace = False) #this line generates order of position of the letter of anagram, replacement of letter is not allowed)
    anagram = ''
    for i in range(len(order)):                 #this combines the letter to anagram according to the position
        anagram = anagram + choice[order[i]]
    return(anagram)
    

anagram = anagramgenerator(word)

def anagramGame():                          #execution of the game
    stop = False                           
    print('***Anagram***\n')
    print('Color word anagram: ',anagram,'\n')  
    while stop == False:    
        userinput = input('Guess the color word: ')
        if userinput != word:
            print('Incorrect, guess again.')
        elif userinput == word:
            stop = True
            print('Correct!')
            
anagramGame()

#-------------------------------------------------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 11:04:54 2016
@author: Tommy Cheng
"""

# Question 10: lingo
'''Game: the is a program that prompts the user to enter a five-letter word. 
   Clue will be given. [] means the letter is the right letter and in right position 
   and () means the letter is the right letter but not in the right position. 
   The restriction on this game is it only allows a word with no repeated letters
'''
print('Welcome to lingo!')
lingo = input('Enter the lingo: ')

stop = False
while stop == False:
    word = input('Enter a 5-letter word: ')
    char_lingo = list(lingo)            #convert lingo into char list
    char_word = list(word)              #convert guess word into char list
    if lingo == word:       #if the word matches with lingo, show lingo
        print('Yes, the word is : '+lingo)
        print('Congrats, you guessed it!')
        break
   
    for i in range(len(char_word)):     #This checks if the letter is the right letter and in right position 
       if char_word[i] == char_lingo[i]:
            hint1 = ('[',char_word[i],']')
            char_word[i] = ''.join(hint1)
            print(char_word[i]) 
       elif char_word[i] in lingo:  #This checks if the letter is the right letter but not in right position 
            hint2 = ('(',char_word[i],')')
            char_word[i] = ''.join(hint2)
    clue = ''.join(char_word)
    print('Clue: ',clue)
#-------------------------------------------------------------------------------------------------------------------------

# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 02:28:13 2016

@author: TCheng
"""
'''Problem 11: This program is a sentence splitter can split a text into
sentences. It will print every sentence in every line
'''
#Stuart- Excellent use of regular expressions, but you need to put this in function form.

import re

text2 = '"Droll?" said Mr. Newman, laughing too. "Did you ever hear of Christopher Columbus?"'
text = "Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it! Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't."


#This is a split function 
#the first argument (?<!\w\.\w.) 
#?<! prevents the split if the following conditions satisfy:
#\w = word character [a-z, A-Z, 0-9_] followed by \. = '.' followed by 
#\w match any word character [a-z, A-Z, 0-9_]
#. matches any character (except newline)

#the second argumnt (?<![A-Z]\.)  
#?<! prevents the split if the following conditions satisfy:
#[A-Z] matchesA-Z a single character in the range between A and Z uppercase followed by
#\. matches the character.

#the third argument (?<![A-Z][a-z]\.)
#?<! prevents the split if the following conditions satisfy:
#A-Z a single character in the range between A and Z upper case followed by 
#[a-z] match a single character present in a-z a single character followed by 
#\. matches the character .

#the fourth argument (?<=\.|\?|\!)\s
#?<= allows the split if the following conditions satisfy:
#\. = '.' or \? = '?' or \! = "!" followed \s = any white space


sentence = re.split('(?<!\w\.\w.)(?<![A-Z]\.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s' , text)


for line in sentence :
    print(line + '\n')
#---------------------------------------------------------------------------------------------
    
"""
Created on Thu Sep 15 19:23:11 2016

@author: Tommy Cheng
"""

"""
Problem 12:  This program finds the sets of words of anagram that share the same characters that
contain the most words in them. 
"""

def anagram() :
	
	content = ""

	# I use with here so file needs not to be close'
	with open('unixdict.txt', 'r') as content_file:
		content = content_file.read()

	# converting 'content' into a list of words
	lst = content.split("\n")

	# coverting list of words to list of wordbank cotaining the original word and sorted word 
	for i in range(0, len(lst)) :
		lst[i] =  { 'word': lst[i], 'sort': ''.join(sorted(lst[i])) } 

	# sort the list in ascending order of the sorted words
	lst.sort(key = lambda x: x['sort'])

	grp = []
	i = 0

	# group the anagrams together in ang[] and check repeated elements
	while i < len(lst) :
		ang = [];
		ang.append(lst[i]['word'])
		while(i+1 < len(lst) and lst[i]['sort'] == lst[i+1]['sort']): 
			i += 1                   
			ang.append(lst[i]['word'])   

		i += 1
		grp.append(ang)

	# sort the list containing group of anagrams in descending order
	grp.sort(key = lambda x : len(x), reverse=True)

	
	i = 0
	while(True):  # print the group of anagrams having maximum number of words
		if (len(grp[i]) == len(grp[1])) :
			print(grp[i])
			i += 1
		else :
			break


anagram()

    
#-------------------------------------------------------------------------------------------------------------------------    
    # -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 17:16:44 2016

@author: TommyCheng
"""

'''Problem 13: This program generates a string with
N opening brackets ("[") and N closing brackets ("]"), in some
arbitrary order. And it prints whether there exists complete pairs of brackets
'''

import random

def generate_string(n):
    string = ''
    for i in range(2*n):                #Here I use a random number generator to generate 
        if random.randint(0,1) == 0:    #open and close brackets
            string += '['
        else:
            string += ']'
    return(string)

def check(string):
    counter = 0;
    for i in range (len(string)):       
        if string[i] == '[':            #Here is a special way of counting, if it starts 
            counter += 1                #with a open bracket, the next bracket can either be open of close, for both cases 
        else:                           # the counter will be greater than zero. After all iterations, if the counter is zero, that means 
            counter -= 1                  #each open brackets closes properly given that the first bracket is open.
            if counter <0:              #if the counter is zero after the first iteration, it must be imcomplete because it starts with a close bracket
                break
            
    if counter == 0:            #If counter = 0, everything checks out
        print(string +'\nOK')
    else:   
        print(string + '\nNotOK')



check( generate_string(1))
check( generate_string(2))
check( generate_string(3))
check( generate_string(4))
#-------------------------------------------------------------------------------------------------------------------------


# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 02:53:21 2016
@author: TommyCheng
"""
'''
This program generates the/a sequence with the highest possible
number of Pokemon names where the subsequent name starts with
the final letter of the preceding name from a givenlist. No Pokemon name is to be
repeated. 
'''



pokeList = ["audino","bagon","baltoy","banette","bidoof", "braviary", "bronzor", "carracosta","charmeleon","cresselia", "croagunk", 
"darmanitan", "deino", "emboar", "emolga", "exeggcute", "gabite", "girafarig", "gulpin", "haxorus", "heatmor", "heatran", "ivysaur", "jellicent", "jumpluff", "kangaskhan","kricketune", "landorus", "ledyba", "loudred", "lumineon", "lunatone", "machamp", "magnezone", "mamoswine","nosepass", "petilil", "pidgeotto", "pikachu", "pinsir", "poliwrath", "poochyena", "porygon2",
"porygonz", "registeel", "relicanth", "remoraid", "rufflet", "sableye", "scolipede", "scrafty", "seaking",
"sealeo", "silcoon", "simisear", "snivy", "snorlax", "spoink", "starly", "tirtouga", "trapinch", "treecko","tyrogue", "vigoroth", "vulpix", "wailord", "wartortle","whismur","wingull" ,"yamask"]

finalList = []  # this is the final list


def solve(newList):
	global finalList,pokeList

	flag = 0
	for name in pokeList:		#search the names in the pokeList 
		if((len(newList) == 0) or (name not in newList and (name[0] == newList[-1][-1]))):
			# this condition checks if newlist is empty or first letter of name mathces last letter of last element of list
			flag = 1 #indicator variable
			newList.append(name) # if so, adds the name and recurs the function again to search for the next pokemon name
			solve(newList)
			# pops the element for backtracking and hence also looks at other possiblities
			newList.pop()
	

	if(flag == 0):
		# flag is 0 if non of the element matches the condition mentioned above, hence our sequence is complete
		#this might not be the longest list 

		if (len(newList) > len(finalList)):   # check for size of current sequence with the final list
			finalList = list(newList)

def main():
	solve([])

	print(len(finalList))
	print("The elements are :")
	for name in finalList:
		print(name)


main();



#-------------------------------------------------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 05:31:32 2016

@author: Tommy Cheng
"""
'''Problem 14: Alternade: This program prints all the alternade of every word in 
the wordbank taken alternatively in a strict sequence, and used in the same order as the original word,
make up at least two other words. All letters are be used, but the
smaller words are not necessarily of the same length. It will not print if the alternade only has fewer than 2 words
'''

file = open('wordlist.txt')
wordbank = file.read().split()
wordlist1, wordlist2 = [], []

smallword_1 = ''
smallword_2 = ''


for word in wordbank:               #go throgh the each word in the wordbank
    smallword_1 = ''                #create a temporary variable to store a small word
    smallword_2 = ''                #create a temp variable to store another small word
    word_1 = ''             #temp variable, check to see if the str is empty, if so it will not print
    word_2 = ''               #same purpose as the above for 

    length = 0
    
    if len(word) == 1:             #Case1: if the word has 1 letter
        print('"' + word + '": makes no word.')
    elif(len(word)>1):              #Case2: if the word has more than 1 letter
        for i in range(len(word)):
            #print(i)
            if i%2==0:                 #extract the even position letter(letter in position, 0, 2, 4, ...)
                smallword_1 = smallword_1 + word[i]   #combine the even position letters to form a word
            elif i%2 ==1:               #extract the odd position letter(letter in position, 1, 3, 5, ...)
                smallword_2 = smallword_2 + word[i] #combine the even position letters to form a word
    for j in range (len(wordbank)):
        if(smallword_1 == wordbank[j]):     #check if smallword 1 exists in the wordbank
            word_1 = wordbank[j]
        elif smallword_2 == wordbank[j]:     #check if smallword 2 exists in the wordbank
            word_2 = wordbank[j];
    


    if word_1 != '' and word_2 !='':        #if both aren't empty, print the strings
        print(word + ' makes ' + word_1 +' and ' + word_2 +'\n')
    
                
#-------------------------------------------------------------------------------------------------------------------------
                
        
