import os
import json
import nltk
import numpy as np
import gensim
import pickle
from gensim import corpora, models,similarities

mode1 = gensim.models.Word2Vec.load('word2vec.bin')
