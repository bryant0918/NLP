# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 11:05:36 2022

@author: Bryant McArthur
"""

import spacy
from spacy.symbols import nsubj, VERB
from spacy import displacy


nlp = spacy.load("en_core_web_sm")
"""
doc = nlp("Autonomous cars shift insurance liability toward manufacturers")
for chunk in doc.noun_chunks:
    print(chunk.text, chunk.root.text, chunk.root.dep_,
            chunk.root.head.text)
    
doc = nlp("Autonomous cars shift insurance liability toward manufacturers")
for token in doc:
    print(token.text, token.dep_, token.head.text, token.head.pos_,
            [child for child in token.children])
    
verbs = set()
for possible_subject in doc:
    if possible_subject.dep == nsubj and possible_subject.head.pos == VERB:
        verbs.add(possible_subject.head)
print(verbs)

verbs = []
for possible_verb in doc:
    if possible_verb.pos == VERB:
        for possible_subject in possible_verb.children:
            if possible_subject.dep == nsubj:
                verbs.append(possible_verb)
                break
print(verbs)


doc = nlp("bright red apples on the tree")
print([token.text for token in doc[2].lefts])  # ['bright', 'red']
print([token.text for token in doc[2].rights])  # ['on']
print(doc[2].n_lefts)  # 2
print(doc[2].n_rights)  # 1

doc = nlp("Credit and mortgage account holders must submit their requests")

root = [token for token in doc if token.head == token][0]
subject = list(root.lefts)[0]
for descendant in subject.subtree:
    assert subject is descendant or subject.is_ancestor(descendant)
    print(descendant.text, descendant.dep_, descendant.n_lefts,
            descendant.n_rights,
            [ancestor.text for ancestor in descendant.ancestors])
    
    
span = doc[doc[4].left_edge.i : doc[4].right_edge.i+1]
with doc.retokenize() as retokenizer:
    retokenizer.merge(span)
for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)
"""
    
nlp.add_pipe("merge_entities")
nlp.add_pipe("merge_noun_chunks")

TEXTS = [
    "Net income was $9.4 million compared to the prior year of $2.7 million.",
    "Revenue exceeded twelve billion dollars, with a loss of $1b.",
]
for doc in nlp.pipe(TEXTS):
    for token in doc:
        if token.ent_type_ == "MONEY":
            # We have an attribute and direct object, so check for subject
            if token.dep_ in ("attr", "dobj"):
                subj = [w for w in token.head.lefts if w.dep_ == "nsubj"]
                if subj:
                    print(subj[0], "-->", token)
            # We have a prepositional object with a preposition
            elif token.dep_ == "pobj" and token.head.dep_ == "prep":
                print(token.head.head, "-->", token)
                
doc = nlp("Autonomous cars shift insurance liability toward manufacturers")
# Since this is an interactive Jupyter environment, we can use displacy.render here
displacy.render(doc, style='dep')
print()
print()


BoM = "\
Wherefore, it is an abridgment of the record of the people of Nephi,\
and also of the Lamanites—Written to the Lamanites, who are a remnant \
of the house of Israel; and also to Jew and Gentile—Written by way of \
commandment, and also by the spirit of prophecy and of \
revelation—Written and sealed up, and hid up unto the Lord, that they \
might not be destroyed—To come forth by the gift and power of God unto \
the interpretation thereof—Sealed by the hand of Moroni, and hid up \
unto the Lord, to come forth in due time by way of the Gentile—The \
interpretation thereof by the gift of God.\
"

BoM2 = "\
An abridgment taken from the Book of Ether also, which is a record of \
the people of Jared, who were scattered at the time the Lord confounded \
the language of the people, when they were building a tower to get to \
heaven—Which is to show unto the remnant of the House of Israel what \
great things the Lord hath done for their fathers; and that they may \
know the covenants of the Lord, that they are not cast off forever—And \
also to the convincing of the Jew and Gentile that JESUS is the CHRIST,\
the ETERNAL GOD, manifesting himself unto all nations—And now, if there \
are faults they are the mistakes of men; wherefore, condemn not the \
things of God, that ye may be found spotless at the judgment-seat of \
Christ. "

Polishtxt = "Ja lubie Placki. I like pancakes.\
Jestem samolotem.\
Gruba kaczka nie może latac.\
Ty jestes grubą kaczką.\
Samolot co ma grubą kaczke spada i exploduje.\
Placki to nowe Hamburgery.\
Gangnam Style jest za popularny\
"

"""
nlp = spacy.load("en_core_web_md")
doc = nlp(BoM)
for chunk in doc.noun_chunks:
    print(chunk.text, chunk.root.text, chunk.root.dep_,
            chunk.root.head.text)
print()
    
for token in doc:
    print(token.text, token.dep_, token.head.text, token.head.pos_,
            [child for child in token.children])

print()    

verbs = set()
for possible_subject in doc:
    if possible_subject.dep == nsubj and possible_subject.head.pos == VERB:
        verbs.add(possible_subject.head)
print(verbs)


root = [token for token in doc if token.head == token][0]
subject = list(root.lefts)[0]
for descendant in subject.subtree:
    assert subject is descendant or subject.is_ancestor(descendant)
    print(descendant.text, descendant.dep_, descendant.n_lefts,
            descendant.n_rights,
            [ancestor.text for ancestor in descendant.ancestors])
    
print()

span = doc[doc[4].left_edge.i : doc[4].right_edge.i+1]
with doc.retokenize() as retokenizer:
    retokenizer.merge(span)
for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)
"""
    
nlp = spacy.load("pl_core_news_md")
    
Polishtxt = "Ja lubie Placki. I like pancakes.\
Jestem samolotem.\
Gruba kaczka nie może latac.\
Ty jestes grubą kaczką.\
Samolot co ma grubą kaczke spada i exploduje.\
Placki to nowe Hamburgery.\
Gangnam Style jest za popularny\
"

doc = nlp(Polishtxt)

    
for token in doc:
    print(token.text, token.dep_, token.head.text, token.head.pos_,
            [child for child in token.children])

print()    

verbs = set()
for possible_subject in doc:
    if possible_subject.dep == nsubj and possible_subject.head.pos == VERB:
        verbs.add(possible_subject.head)
print(verbs)


root = [token for token in doc if token.head == token][0]
subject = list(root.lefts)[0]
for descendant in subject.subtree:
    assert subject is descendant or subject.is_ancestor(descendant)
    print(descendant.text, descendant.dep_, descendant.n_lefts,
            descendant.n_rights,
            [ancestor.text for ancestor in descendant.ancestors])
    
print()

span = doc[doc[4].left_edge.i : doc[4].right_edge.i+1]
with doc.retokenize() as retokenizer:
    retokenizer.merge(span)
for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)

