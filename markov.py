#!/usr/bin/python
#based on http://codelikebozo.com/markov-chains-in-python
from __future__ import with_statement
import random
import sys
 
def create_chain(file_paths):
    markov_chain = {}
    word1 = "\n"
    word2 = "\n"
    for path in file_paths:
        with open(path) as file:
            for line in file:
                for current_word in line.split():
                    if current_word != "":
                        markov_chain.setdefault((word1, word2), []).append(current_word)
                        word1 = word2
                        word2 = current_word
    return markov_chain
 
def construct_sentence(markov_chain, word_count=30):
    generated_sentence = ""
    word_tuple = random.choice(markov_chain.keys())
    w1 = word_tuple[0]
    w2 = word_tuple[1]
    
    for i in xrange(word_count):
        #"total count" is a special key used to track word frequency.
        newword = random.choice(markov_chain[(w1, w2)])
        generated_sentence = generated_sentence + " " + newword
        w1 = w2
        w2 = newword
        
    return generated_sentence
 
markov = create_chain((sys.argv[1:]))
#print markov
print construct_sentence(markov_chain = markov, word_count=100)
