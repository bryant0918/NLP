# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 14:27:53 2022

@author: bryant McArthur
"""


from nltk.parse.generate import generate, demo_grammar
from nltk.parse import RecursiveDescentParser
from nltk import CFG
grammar = CFG.fromstring(demo_grammar)
print(grammar)


for sentence in generate(grammar, n=10):
    print(' '.join(sentence))

print()

for sentence in generate(grammar, depth=4):
    print(' '.join(sentence))
    
print()

print(len(list(generate(grammar, depth=3))))
print(len(list(generate(grammar))))

from nltk.grammar import CFG

grammar_string = '''
S -> NP VP
PP -> P NP
D -> 'the'
PN -> 'saumya'|'dinesh'
PRO -> 'she'|'he'|'we'
A -> 'tall'|'naughty'|'long'|'three'|'black'
P -> 'with'|'in'|'from'|'at'
QP -> 'some'
'''

grammar = CFG.fromstring(grammar_string)
print(grammar)


grammar_string = '''
S -> NP VP
NP -> PN | PRO | D N | D A N | D N PP | QP N | A N | D NOM PP | D NOM
VP -> 'fished'
VP -> 'bait' NP
VP -> 'slept'
VP -> 'saw' NP
VP -> 'walked' PP
VP -> 'wanted_to_fish_for' NP



NP -> 'fish'|'bait'
PP -> P NP
PN -> 'saumya'|'dinesh'|'Bryant'
PRO -> 'she'|'he'|'we'
A -> 'tall'|'naughty'|'long'|'three'|'black'
P -> 'with'|'in'|'from'|'at'
QP -> 'some'

D -> D_def | D_sg
D_def -> 'the'
D_sg -> 'a'

N -> N_sg | N_pl
N_sg -> 'boy'|'girl'|'room'|'garden'|'hair'
N_pl -> 'dogs'|'cats'
'''

grammar = CFG.fromstring(grammar_string)
print(grammar)

rdparser = RecursiveDescentParser(grammar)
sent = "Bryant wanted_to_fish_for bait".split()
trees = rdparser.parse(sent)

for tree in trees:
    print ("Tree", tree)
    
for sentence in generate(grammar, n=10):
    print(' '.join(sentence))


    
#grammar = CFG.fromstring("""
"""
S -> NP VP

S -> S SCMP 

SCMP -> THAT S 

S -> S SCNJ 

SCNJ -> SCONJ S 

NP -> DET N | NUMB N | AP N | N N | N | N PP 

NP -> PRON 

NP -> NP CONJ NP 

VP -> VP PP 

AP -> ADV ADJ | ADJ 

PP -> P NP 

VP -> MODAL V | ADV V | V V | V NP | V AP | V PP 

VP -> V NP NP 

"""

#)

#print(len(list(generate(grammar))))








"""

import benepar
import spacy
import nltk
benepar.download('benepar_en3_large')


nlp = spacy.load('en_core_web_md')


print(spacy.__version__.startswith('2'))

if spacy.__version__.startswith('2'):
        nlp.add_pipe(benepar.BeneparComponent("benepar_en3"))
else:
    nlp.add_pipe("benepar", config={"model": "benepar_en3"})
doc = nlp("The time for action is now. It's never too late to do something.")
sent = list(doc.sents)[0]
print(sent._.parse_string)
sent._.labels

list(sent._.children)[0]





nlp.add_pipe(benepar.BeneparComponent("benepar_en3_large"))
#nlp.add_pipe('benepar', config={'model': 'benepar_en3'})
doc = nlp('The time for action is now. It is never too late to do something.')
sent = list(doc.sents)[0]
print(sent._.parse_string)
# (S (NP (NP (DT The) (NN time)) (PP (IN for) (NP (NN action)))) (VP (VBZ is) (ADVP (RB now))) (. .))
print(sent._.labels)
# ('S',)
print(list(sent._.children)[0])
# The time for action

"""