# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 13:29:54 2022

@author: bryant McArthur
"""

import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            token.shape_, token.is_alpha, token.is_stop)

