# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 15:26:34 2022

@author: bryant McArthur
"""
"""
import nltk
from nltk.book import text3


def corpus():
    
    for line in open("file.txt"):
        for word in line.split():
            if word.endswith('ing'):
                print(word)
            else:
                line.split().remove(word)
"""

import numpy as np


def MonteCristo(filename1,filename2):
    with open(filename1, 'r',encoding = "utf-8") as myfile:
        '''Algorithm 1.1'''
        sentences = myfile.read().split('\n') 
        uniquewords = set()
        # get the set of unique words
        for sentence in sentences:
            words = sentence.split()
            uniquewords.update(words)  
            
        print(len(uniquewords))
        
        ly = []
        for word in uniquewords:
            if word.endswith('ly'):
                ly.append(word)
        
        print(len(ly))
        
        
    with open(filename2, 'r',encoding = "utf-8") as myfile:
        '''Algorithm 1.1'''
        sentences = myfile.read().split('\n') 
        uniquewords2 = set()
        # get the set of unique words
        for sentence in sentences:
            words = sentence.split()
            uniquewords2.update(words)  
            
        print(len(uniquewords2))
        
        ly2 = []
        for word in uniquewords2:
            if word.endswith('ly'):
                ly2.append(word)
        
        print(len(ly2))
        
    
    intersection = []
    for adverb in ly:
        for word in ly2:
            if adverb == word:
                intersection.append(word)
                ly2.remove(word)
    print(len(intersection))
                
                
    words = []
    u1 = list(uniquewords)
    u2 = list(uniquewords2)
    for word in u1:
        if word in uniquewords2:
            words.append(word)
                
    
    print(len(words))
    print(ly)
    x = "\n".join(ly)
    with open("BoM Adverbs.txt",mode='w') as myfile:
            myfile.write(x)

            
# Problems 3 and 4: Write a 'ContentFilter' class.
"""Class for reading in file
        
    Attributes:
        filename (str): The name of the file
        contents (str): the contents of the file
        
    """
class ContentFilter(object):   
    # Problem 3
    def __init__(self, filename):
        """Read from the specified file. If the filename is invalid, prompt
        the user until a valid filename is given.
        """
        valid = False
        while not valid:
            try:
                with open(filename, 'r') as myfile:
                    self.filename = myfile.name
                    self.contents = myfile.read()
                valid = True
            except:
                filename = input("Please enter a valid file name:")
                
 # Problem 4 ---------------------------------------------------------------
    def check_mode(self, mode):
        """Raise a ValueError if the mode is invalid."""
        if mode not in ['w', 'x', 'a']:
            raise ValueError("the mode is invalid")

    def uniform(self, outfile, mode='w', case='upper'):
        """Write the data to the outfile in uniform case."""
        
        self.check_mode(mode)
        
        data = self.contents
        if case == 'upper':
            data = data.upper()
        elif case == 'lower':
            data = data.lower()
        else:
            raise ValueError("Must be upper or lower case")
        
        with open(outfile, mode) as myfile:
            myfile.write(data)


    def reverse(self, outfile, mode='w', unit='line'):
        """Write the data to the outfile in reverse order."""
        self.check_mode(mode)
        
        data = self.contents
        newdata = []
        
        #Switching all the words on each line
        if unit=="word":
            
            newdata = data.split('\n')
            
            for i in range(len(newdata)):
                superdata = newdata[i].split()
                superdata.reverse()
                newdata[i] = " ".join(superdata)
            
            x = "\n".join(newdata)
        
        #switching just the lines
        elif unit=='line':
            newdata = data.split('\n')
            newdata.reverse()
            x = "\n".join(newdata)
        else:
            raise ValueError("Must be line or word")
        
        #Write the data to the outfile
        with open(outfile, mode) as myfile:
            myfile.write(x)
        
        
    def transpose(self, outfile, mode='w'):
        """Write the transposed version of the data to the outfile."""
        self.check_mode(mode)
        
        #Open the contents and immediately put it into an array
        with open(self.filename, 'r') as inputfile:
            with open(outfile, mode) as myfile:
                x = np.loadtxt(inputfile, dtype = str)
                xtrans = x.T
        
        #Take the transpose of the data as a list
        data = xtrans.tolist()
        
        #Join the words
        for i in range(len(data)):
            newdata = data[i]
            data[i] = " ".join(newdata)
        #Join the lines
        x = "\n".join(data)
        
        #Write it to the outfile
        with open(outfile, mode) as myfile:
            myfile.write(x)
        
        

    def __str__(self):
        """String representation: info about the contents of the file."""
        
        s = ""
        s = s + "Source file:\t\t\t"+self.filename + "\n"
        s = s + "Total Characters: \t\t" + str(len(self.contents)) + "\n"
        s = s + "Alphabetic characters: \t" + str(sum(k.isalpha() for k in self.contents)) + "\n"
        s = s + "Numerical chcaracters: \t" + str(sum(k.isdigit() for k in self.contents)) + "\n"
        s = s + "Whitespace characters: \t" + str(sum(k.isspace() for k in self.contents)) + "\n"
        s = s + "Number of lines: \t\t" + str(self.contents.count("\n"))
        
        return s
        



if __name__ == "__main__":
    MonteCristo("The Book of Mormon.txt","Count of Monte Cristo.txt")
    pass



                



