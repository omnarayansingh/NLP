# -*- coding: utf-8 -*-
"""spacy_vs_nltl.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_jSN3qm0MI_N5CAC5MyUhP5jd4orvtoq
"""

!pip install spacy

!python -m spacy download en_core_web_sm

import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("Dr. Strange loves pav bhaji of mumbai. Hulk loves chat of Delhi")

for Sentence in doc.sents:
  print(Sentence)

for token in doc:
  print(token, "|", token.pos_,"|", token.lemma_)

for ent in doc.ents:
  print(ent.text, "|", ent.label_, "|",spacy.explain(ent.label_))

!pip install nltk

import nltk
nltk.download('punkt')

from nltk.tokenize import sent_tokenize

sent_tokenize("Dr. Strange loves pav bhaji of mumbai. Hulk loves chat of Delhi")