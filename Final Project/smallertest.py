# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 13:37:03 2022

@author: bryan
"""

def smallertest(file):
    """Create a test that runs quicker with 1% of the sentences"""
    with open(file, 'r', encoding = 'utf-8') as f:
        data = f.readlines()
        
    smtest = []
        
    for i in range(len(data)):
        if i %100 == 0:
            smtest.append(data[i])
            
    with open("smtesttgt.txt", 'w', encoding = 'utf-8') as out:
        out.writelines(smtest)
        

def smallerval(src_file, tgt_file):
    """Create a smaller validation set of only 3000 lines that runs quicker."""
    with open(src_file, 'r', encoding = 'utf-8') as f:
        src_data = f.readlines()
        
    with open(tgt_file, 'r', encoding = 'utf-8') as f:
        tgt_data = f.readlines()
        
    sm_src_val = []
    sm_tgt_val = []
    
    for i in range(len(src_data)):
        if i%66 == 0:
            sm_src_val.append(src_data[i])
            sm_tgt_val.append(tgt_data[i])
            
    with open("Csmsrc-test.txt", 'w', encoding = 'utf-8') as out:
        out.writelines(sm_src_val)
        
    with open("Csmtgt-test.txt", 'w', encoding = 'utf-8') as out:
        out.writelines(sm_tgt_val)
        
        
        
def factoroften(file):
    """Break a file down by one-tenth the size for testing"""
    with open(file, 'r', encoding = 'utf-8') as f:
        data = f.readlines()
        
    smtest = []
        
    for i in range(len(data)):
        if i %10 == 0:
            smtest.append(data[i])
            
    with open(file+"2.txt", 'w', encoding = 'utf-8') as out:
        out.writelines(smtest)
    
        
if __name__ == "__main__":
    #smallertest("Ttgt-test.txt")
    #smallerval("Multi Model/nottoy-enpl/Csrc-test.txt", "Multi Model/nottoy-enpl/Ctgt-test.txt")
    #factoroften("Full OG Tokenized text/Cz_tok_val.txt")
    #factoroften("Cz_tok_val.txt")
    #factoroften("Full OG Tokenized text/En_tok_test.txt")
    #factoroften("En_tok_val.txt")
    #factoroften("Full OG Tokenized text/Es_tok_test.txt")
    #factoroften("Es_tok_val.txt")
    #factoroften("Full OG Tokenized text/Pl_tok_val.txt")
    #factoroften("Pl_tok_val.txt")
    #factoroften("Es-Cz Model/tgt-test.txt")
    #factoroften("Es-Cz Model/src-test.txt")
    
    
    
    
    
    
    
    
    
    
    
    