# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 14:04:09 2022

@author: Bryant McArthur
"""

import html
import re
        
def clean_lines(file):
    """Go by line to hopefully not completely delete lines"""
    #Read in the text
    with open(file, 'r', encoding = 'utf-8') as myfile:
        lines = myfile.readlines()
        
    with open("hyphen.txt", 'r', encoding = 'utf-8') as data:
        characters = data.read()
        hyphen1 = characters[0]
        hyphen2 = characters[1]
        others = characters[2:]
        
    with open("nonbreakingspace.txt", 'r', encoding = 'utf-8') as data:
        nbs = data.read()
        
        cleaned = []
        print(len(lines))
        for text in lines:
            #Get rid of HTML characters
            newtext = html.unescape(text)
            text = html.unescape(newtext)
            
            """Using Regex"""
            #For weird % issues
            text = re.sub(r"(%\S\s|\s%\s|%.*%|%\S)", "", text)
            
            #Get rid of dumb Hyphens and make them dashes
            text = text.replace(hyphen1, "-")
            text = text.replace(hyphen2, "-")
            
            #For random characters I don't want anywhere
            text = text.replace(others,"")
            #text = text.replace(nbs," ")
            
            #For weird characters at the beginning of the line
            rando = re.compile(r"(^[,#)*-.\s\\\/]\s?)", re.MULTILINE)
            text = rando.sub(r"", text)
            beg = re.compile(r"^\W+",re.MULTILINE)
            text = beg.sub(r"",text)
            numbers = re.compile(r"^[\d\s]*")
            text = numbers.sub(r"", text)
            
            #Get rid of all nonword characters at the end of the line
            end = re.compile(r"\W+$", re.MULTILINE)
            text = end.sub(r"",text)
            numbers = re.compile(r"[\s\d\W]*$")
            text = numbers.sub(r"", text)
            
            #All extra space at the beginning and end of the line
            space = re.compile(r"^\s+", re.MULTILINE)
            space2 = re.compile(r"\s+$", re.MULTILINE)
            text = space.sub(r"", text)
            text = space2.sub(r"", text)
            
            #Ignore Case
            text = text.casefold()
            
            cleaned.append(text+"\n")
            
        print(len(cleaned))
        
        
    with open(file+"clean.txt",'w', encoding = 'utf-8') as myfile:
        myfile.writelines(cleaned)
    
    
def excess(file1, file2):
    """Get rid of lines that are too short or too long"""
    
    with open(file1, 'r', encoding = 'utf-8') as myfile:
        lines1 = myfile.readlines()
        
    with open(file2, 'r', encoding = 'utf-8') as myfile:
        lines2 = myfile.readlines()
        
        
    cleaned1 = []
    cleaned2 = []
    
    for i in range(len(lines1)):
        if (3 <= len(lines1[i].split()) <= 100) and (3 <= len(lines2[i].split()) <= 100):
            cleaned1.append(lines1[i])
            cleaned2.append(lines2[i])
            
    print(len(cleaned1), len(cleaned2))
    
    with open("Es_clean.txt",'w', encoding = 'utf-8') as myfile:
        myfile.writelines(cleaned1)
        
    with open("Pl_clean.txt",'w', encoding = 'utf-8') as myfile:
        myfile.writelines(cleaned2)
        


    
    
if __name__ == "__main__":
    
    """Clean"""
# =============================================================================
#     clean_lines("Es.txt")
#     clean_lines("Pl.txt")
# =============================================================================
    
# =============================================================================
#     clean_lines("Es.txtclean.txtclean.txt")
#     clean_lines("Pl.txtclean.txtclean.txt")
# =============================================================================
    
    #excess("Es.txtclean.txtclean.txtclean.txt", "Pl.txtclean.txtclean.txtclean.txt")
    
 