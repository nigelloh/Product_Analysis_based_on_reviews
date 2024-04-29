import pandas as pd
import re
from nltk.corpus import stopwords
from nltk import ngrams
import math
from collections import Counter

def processing(text):

    stop_words = stopwords.words('english')

    # implement subtask 1
    text = re.sub('[^a-zA-Z\s\r\n]+', ' ', text)
    
    # implement subtask 2
    text = re.sub('[\s\r\n]+', ' ', text)

    # implement subtask 3
    text = text.lower()

    # implement subtask 4 and 5
    text_set = text.split()
    text_list = []
    for word in text_set:
        if (len(word) > 2) and (word not in stop_words):
            text_list.append(word)

    # implement subtask 6
    bigrams = [f"{word1} {word2}" for word1, word2 in ngrams(text_list, 2)]
    bigrams = list(dict.fromkeys(bigrams))
    
    return bigrams
