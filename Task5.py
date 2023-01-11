# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 10:59:48 2022

@author: Bryant McArthur
"""

import eng_to_ipa as ipa


my_str = "The quick brown fox jumped over the lazy dog."
print(ipa.convert(my_str))
print(ipa.ipa_list(my_str))
print(ipa.isin_cmu(my_str))
#print(ipa.get_rhymes(my_str))
print(ipa.get_rhymes("Bryant"))
print(ipa.isin_cmu("Bryant"))



def eng2ipa(filename):
    """Convert English file text to IPA"""
    
    with open(filename, 'r', encoding = "utf-8") as file:
        mystring = file.read()
        
        myipa = ipa.convert(mystring)
        
        with open("Monte Cristo IPA.txt",mode='w',encoding = "utf-8") as myfile:
            myfile.write(myipa)
        
eng2ipa("Monte Cristo Chapter 1.txt")



