# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 13:35:18 2022

@author: Bryant McArthur
"""

import random
from sklearn.model_selection import train_test_split
import re



def split(n, file, src = True):
    """
    Choose numbers so that after split there are about 2500 in test and validation sets.
    """
    with open(file, 'r', encoding = "utf-8") as myfile:
        text = myfile.readlines()
    
    test = []
    train = []
    val = []
    
    #Split evenly
    for i in range(len(text)):
        if i % n == 0:
            test.append(text[i])
        elif i % n == n//2:
            val.append(text[i])
        else:
            train.append(text[i])
    
    
    if src:
        with open("src-test.txt", 'w', encoding = "utf-8") as outfile:
            outfile.writelines(test)
        
        with open("src-train.txt", 'w', encoding = "utf-8") as outfile:
            outfile.writelines(train)
            
        with open("src-val.txt", 'w', encoding = "utf-8") as outfile:
            outfile.writelines(val)
            
        return test, val, train
        
    else:
        with open("tgt-test.txt", 'w', encoding = "utf-8") as outfile:
            outfile.writelines(test)
        
        with open("tgt-train.txt", 'w', encoding = "utf-8") as outfile:
            outfile.writelines(train)
            
        with open("tgt-val.txt", 'w', encoding = "utf-8") as outfile:
            outfile.writelines(val)
            
        return test, val, train
    


    
        
if __name__ == "__main__":
    
# =============================================================================
#     split("Pl_tok.txt",True)
#     split("Es_tok.txt",False)
# =============================================================================
  
    
    pass
    
    
    
    
    
    
    
    