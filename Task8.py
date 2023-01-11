# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 12:38:54 2022

@author: Bryant McArthur
"""

import spacy
from spacy.vocab import Vocab
import numpy as np

nlp = spacy.load("en_core_web_sm")

doc = nlp("Apple sold something to the U.K. for like $1 billion.")

"""
for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            token.shape_, token.is_alpha, token.is_stop)
"""

nlp = spacy.load("en_core_web_md")

"""
doc = nlp("This is a sentence. This is another sentence.")
assert doc.has_annotation("SENT_START")
for sent in doc.sents:
    print(sent.text)

for token in doc:
    print(token.text, token.has_vector, token.vector_norm, token.is_oov)
"""

doc1 = nlp("I like salty fries and hamburgers.")
doc2 = nlp("Fast food tastes very good.")
doc3 = nlp("Mormon Baptist Catholic Buddhist agnostic biscuit gravy tortoise hare pennies quarters large tiny gigantic their there earlobe ear face peanut butter nutella three one seven acronym backwards forward capitol capital ran")

# Similarity of two documents
#print(doc1, "<->", doc2, doc1.similarity(doc2))
# Similarity of tokens and spans
french_fries = doc1[2:4]
burgers = doc1[5]
#print(french_fries, "<->", burgers, french_fries.similarity(burgers))

#print(doc1, "<->", doc3, doc1.similarity(doc3))


n = len(doc3)
for i, token in enumerate(doc3):
    for j, token2 in enumerate(doc3):
        if i < j:
            if token != token2:
                print(token.text, "<->", token2.text, token.similarity(token2))


print(doc3[0])

print(doc3[2].similarity(doc3[0].vector+doc[1].vector.resize(300,)))


vector_data = {
    "dog": np.random.uniform(-1, 1, (300,)),
    "cat": np.random.uniform(-1, 1, (300,)),
    "orange": np.random.uniform(-1, 1, (300,))
}
vocab = Vocab()
for word, vector in vector_data.items():
    vocab.set_vector(word, vector)
    print(len(vocab))

#print(vocab.get_vector("dog"))

    
