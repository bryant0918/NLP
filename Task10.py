# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 12:12:03 2022

@author: bryan
"""

import nltk

from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *

nltk.download('subjectivity')
nltk.download('punkt')
nltk.download('vader_lexicon')

n_instances = 100
subj_docs = [(sent, 'subj') for sent in subjectivity.sents(categories='subj')[:n_instances]]
obj_docs = [(sent, 'obj') for sent in subjectivity.sents(categories='obj')[:n_instances]]
print(len(subj_docs), len(obj_docs))

print(subj_docs[0])

train_subj_docs = subj_docs[:80]
test_subj_docs = subj_docs[80:100]
train_obj_docs = obj_docs[:80]
test_obj_docs = obj_docs[80:100]
training_docs = train_subj_docs+train_obj_docs
testing_docs = test_subj_docs+test_obj_docs

sentim_analyzer = SentimentAnalyzer()
all_words_neg = sentim_analyzer.all_words([mark_negation(doc) for doc in training_docs])

unigram_feats = sentim_analyzer.unigram_word_feats(all_words_neg, min_freq=4)
print(len(unigram_feats))
sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)

training_set = sentim_analyzer.apply_features(training_docs)
test_set = sentim_analyzer.apply_features(testing_docs)

trainer = NaiveBayesClassifier.train
classifier = sentim_analyzer.train(trainer, training_set)

#Training Classifier
for key,value in sorted(sentim_analyzer.evaluate(test_set).items()):
    print('{0}: {1}'.format(key, value))
      
print()

from nltk.sentiment.vader import SentimentIntensityAnalyzer
sentences = ["VADER is smart, handsome, and funny.", # positive sentence example
    "VADER is smart, handsome, and funny!", # punctuation emphasis handled correctly (sentiment intensity adjusted)
    "VADER is very smart, handsome, and funny.",  # booster words handled correctly (sentiment intensity adjusted)
    "VADER is VERY SMART, handsome, and FUNNY.",  # emphasis for ALLCAPS handled
    "VADER is VERY SMART, handsome, and FUNNY!!!",# combination of signals - VADER appropriately adjusts intensity
    "VADER is VERY SMART, really handsome, and INCREDIBLY FUNNY!!!",# booster words & punctuation make this close to ceiling for score
    "The book was good.",         # positive sentence
    "The book was kind of good.", # qualified positive sentence is handled correctly (intensity adjusted)
    "The plot was good, but the characters are uncompelling and the dialog is not great.", # mixed negation sentence
    "A really bad, horrible book.",       # negative sentence with booster words
    "At least it isn't a horrible book.", # negated negative sentence with contraction
    ":) and :D",     # emoticons handled
    "",              # an empty string is correctly handled
    "Today sux",     #  negative slang handled
    "Today sux!",    #  negative slang with punctuation emphasis handled
    "Today SUX!",    #  negative slang with capitalization emphasis
    "Today kinda sux! But I'll get by, lol" # mixed sentiment example with slang and constrastive conjunction "but"
]
paragraph = "It was one of the worst movies I've seen, despite good reviews. \
... Unbelievably bad acting!! Poor direction. VERY poor production. \
... The movie was bad. Very bad movie. VERY bad movie. VERY BAD movie. VERY BAD movie!"

from nltk import tokenize
lines_list = tokenize.sent_tokenize(paragraph)
sentences.extend(lines_list)

tricky_sentences = [
    "Sentiment analysis has never been good.",
    "Sentiment analysis with VADER has never been this good.",
    "Warren Beatty has never been so entertaining.",
    "I won't say that the movie is astounding and I wouldn't claim that \
    the movie is too banal either.",
    "I like to hate Michael Bay films, but I couldn't fault this one",
    "I like to hate Michael Bay films, BUT I couldn't help but fault this one",
    "It's one thing to watch an Uwe Boll film, but another thing entirely \
    to pay for it",
    "The movie was too good",
    "This movie was actually neither that funny, nor super witty.",
    "This movie doesn't care about cleverness, wit or any other kind of \
    intelligent humor.",
    "Those who find ugly meanings in beautiful things are corrupt without \
    being charming.",
    "There are slow and repetitive parts, BUT it has just enough spice to \
    keep it interesting.",
    "The script is not fantastic, but the acting is decent and the cinematography \
    is EXCELLENT!",
    "Roger Dodger is one of the most compelling variations on this theme.",
    "Roger Dodger is one of the least compelling variations on this theme.",
    "Roger Dodger is at least compelling as a variation on the theme.",
    "they fall in love with the product",
    "but then it breaks",
    "usually around the time the 90 day warranty expires",
    "the twin towers collapsed today",
    "However, Mr. Carter solemnly argues, his client carried out the kidnapping \
    under orders and in the ''least offensive way possible.''"
]
sentences.extend(tricky_sentences)
"""
for sentence in sentences:
     sid = SentimentIntensityAnalyzer()
     print(sentence)
     ss = sid.polarity_scores(sentence)
     for k in sorted(ss):
         print('{0}: {1}, '.format(k, ss[k]), end='')
     print()
"""

print()


my_sentences = [
    "These are now my sentences and they rock.",
    "This movie sucks, so you'd probably like it",
    "Your favorite restaurant has the grossest pizza ever.",
    "Why do you even like that?",
    "Do you ever get annoyed when you're typing on the bottom of the screen",
    "You're funny",
    "Oh boy that's so hilarious *Sarcastically",
    "Your sarcasm really turns me on",
    "I'm just the kinda guy who loves cheap boring dates",
    "All babies you call cute look like aliens"    
    ]


sentences.extend(my_sentences)
"""
for sentence in sentences:
    sid = SentimentIntensityAnalyzer()
    print(sentence)
    ss = sid.polarity_scores(sentence)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
        print()
"""

Reviews = [
    "Why do I want to write the 234th comment on The Shawshank Redemption? I am not sure - almost everything that could be possibly said about it has been said. But like so many other people who wrote comments, I was and am profoundly moved by this simple and eloquent depiction of hope and friendship and redemption.",
    "One of the best films of all time, an absolute masterpiece. The Godfather is arguably the best gangster drama as well as setting the standard for cinema.",
    "Confidently directed, dark, brooding, and packed with impressive action sequences and a complex story, The Dark Knight includes a career-defining turn from Heath Ledger as well as other Oscar worthy performances, TDK remains not only the best Batman movie, but comic book movie ever created.",
    "Hold your ground, hold your ground! Sons of Gondor, of Rohan, my brothers! I see in your eyes the same fear that would take the heart of me. A day may come when the courage of men fails, when we forsake our friends and break all bonds of fellowship, but it is not this day. An hour of wolves and shattered shields, when the age of men comes crashing down! But it is not this day! This day we fight! By all that you hold dear on this good Earth, I bid you *stand, Men of the West!*",
    "I admit it, I love all three Lord of the Rings films. People may say Return of the King is the best of the trilogy, some may say it is the worst. I personally think Two Towers is the best for its scope and better exploration of some of the characters, but while it is still great Return of the King is better than Fellowship of the Ring.",
    "I'd thought I'd never see the day when I'd see something worse than Home Alone 4, but with this monstrosity, it just goes to show how much I could be proved wrong.",
    "Okay, the first movie from this series \"Baby Geniuses\" was so poorly received that reviewers were beside themselves castigating the film. It currently is ranked #73 on the IMDb Bottom 100 list. Yet, astoundingly, the film led to this even worse sequel--\"Baby Geniuses 2\"! This sort of sequel is a prime example how some people in Hollywood just need to get real jobs...or at least stop doing LSD! Unlike the first horrible piece of garbage that is \"Baby Geniuses\"",
    "It's the most awful movie I've ever seen. From the beginning till the end just the propaganda of the dictator Erdogan in Turkey. There is no sense in the most of the scenes and the expectations of the viewers are not filled at all. Thus, the movie had a free entrance for a week. It's a shame for the country, which mentions to be a democratic one. Very stupid end, very stupid story",
    "I can confirm that I no longer fear Hell for I have seen something much worse. This film is so bad it just wretches you with extreme agony and torture until your eyeballs bleed. I haven't even bothered to rate this because even rating this film \"0\" is too high.",
    "Frankly, I am outraged to see so many 10s for this movie, being that no sane person would ever give such a grade to this unrelentinly boring piece of ... (man, it's quite hard not to use profanity with a movie like this). If people were giving Manos 10s just so that some rival could snatch the #1 worst movie title then that is truly sad. Manos is morally the true winner here in that respect.",
    ]


sentences.extend(Reviews)
for sentence in sentences:
    sid = SentimentIntensityAnalyzer()
    print(sentence)
    ss = sid.polarity_scores(sentence)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
        print()




































