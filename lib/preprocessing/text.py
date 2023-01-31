"""Description. Text preprocessing techniques."""

from typing import List

import string

import nltk
nltk.download("punkt")
nltk.download("stopwords")

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

porter = PorterStemmer()

from spacy.lang.fr.stop_words import STOP_WORDS as fr_stop

STOPLIST = list(set(stopwords.words("french") + list(fr_stop)))
STOPLIST.remove("pas")
STOPLIST.append("’")
STOPLIST.append("«")
STOPLIST.append("»")

def tokenize(text: str) -> List: 
    """Description. Convert text into list of tokens."""

    pattern = r"(\w+|[^\w\s]+)"
    tokens = nltk.regexp_tokenize(text.lower(), pattern)

    return tokens

def remove_punctuation(tokens: List) -> List: 
    """Description. Remove punctuation from list of words."""

    new_tokens = [] 

    for word in tokens:
        for character in string.punctuation:
            word = word.replace(character, "")
        if word != "":
            new_tokens.append(word)
    
    return new_tokens

def remove_stopwords(tokens: List) -> List: 
    """Description. Remove French stopwords from tokens."""

    return [word for word in tokens if word not in STOPLIST]

def stem(tokens: List) -> List: 
    """Description. Chops off the end of words in a tweet."""

    return [porter.stem(word) for word in tokens] 
