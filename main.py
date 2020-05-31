# NCG


# Keras and TF Imports
from tensorflow import keras
import tensorflow as tf
import numpy as np

# NLTK Imports
import nltk
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

print("NLTK Version: {}".format(nltk.__version__))


tags = ["CC",
        "CD",
        "DT",
        "EX",
        "FW",
        "IN",
        "JJ",
        "JJS",
        "LS",
        "MD",
        "NN",
        "NNS",
        "NNP",
        "NNPS",
        "PDT",
        "POS",
        "PRP",
        "PRP$",
        "RB",
        "RBR",
        "RBS",
        "RP",
        "TO",
        "UH",
        "VB",
        "VBD",
        "VBG",
        "VBN",
        "VBP",
        "VBZ",
        "WDT",
        "WP",
        "WP$",
        "WRB"]

descriptions = [
    "Coordinating conjunction",
    "Cardinal number",
    "Determiner",
    "Existential there",
    "Foreign word",
    "Preposition or subordinating conjunction",
    "Adjective",
    "Adjective, comparative",
    "Adjective, superlative",
    "List item marker",
    "Modal",
    "Noun, singular or mass",
    "Noun, plural",
    "Proper noun, singular",
    "Proper noun, plural",
    "Predeterminer",
    "Possessive ending",
    "Personal pronoun",
    "Possessive pronoun",
    "Adverb",
    "Adverb, comparative",
    "Adverb, superlative",
    "Particle",
    "Symbol",
    "to",
    "Interjection",
    "Verb, base form",
    "Verb, past tense",
    "Verb, gerund or present participle",
    "Verb, past participle",
    "Verb, non-3rd person singular present",
    "Verb, 3rd person singular present",
    "Wh-determiner",
    "Wh-pronoun",
    "Possessive wh-pronoun",
    "Wh-adverb"
]
text = "Hello, my name is Ryan. I am able to run for three hours."

solved = pos_tag(word_tokenize(text))

wordTag = []

for tag in solved:
    if tag[1] in tags:
        wordTag.append(tag[1])
        # This is checking the index of the tags so that it can be replaced and more descriptive
        indexPlace = tags.index(tag[1])
        print("Word: {} || Description: {}".format(
            tag[0], descriptions[indexPlace]))
wordCipher = ""
for wordtag in wordTag:
    wordCipher = wordCipher + wordtag + " "
print(wordCipher)

# The word cipher is the cipher that we will use to train the AI.


# Nerual Network Part:
