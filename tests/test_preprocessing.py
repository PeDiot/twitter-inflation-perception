from lib.preprocessing.utils import (
    _string_to_float, 
    _to_datetime, 
)
from lib.preprocessing.tweets import (
    _remove_links, 
    _remove_mentions, 
    _remove_tweet_indicators,
    _remove_tweet_statistics, 
    _remove_tweet_date, 
    clean_tweet, 
)
from lib.preprocessing.text import (
    tokenize, 
    remove_punctuation, 
    remove_stopwords, 
)

from datetime import datetime

import pytest 

def test_string_to_float(): 
    assert _string_to_float("34") == 34.
    assert _string_to_float(34) == 34. 
    assert _string_to_float("15K") == 15000.
    assert _string_to_float("12.92k") == 12920.

    with pytest.raises(ValueError):
        _string_to_float("34a")

def test_to_datetime(): 
    input = "2020-01-01T07:41:04.000Z"
    assert type(_to_datetime(input)) == datetime
    assert _to_datetime(input).strftime("%Y-%m-%d") == "2020-01-01"

    input = "2020-01-0107:41:04.000Z"
    with pytest.raises(ValueError):
        _to_datetime(input)

def test_remove_mentions(): 
    tweet = "Working on a python project with @joe"
    assert _remove_mentions(tweet) == "Working on a python project with "

def test_remove_links(): 
    tweet = "Go to https://stackoverflow.com/ to get accurate answers"
    assert _remove_links(tweet) == "Go to  to get accurate answers"

    tweet = "DeepL uses neural networks to translate sentences. Check it out here: www.deepl.com/translator."
    assert _remove_links(tweet) == "DeepL uses neural networks to translate sentences. Check it out here: "

def test_remove_tweet_indicator(): 
    tweet = "Replying to \n@zeujahh \nHow old are you ?"
    assert _remove_tweet_indicators(tweet) == " \n@zeujahh \nHow old are you ?"

    tweet = "Show this thread \nHere is my complete guide to crypto: "
    assert _remove_tweet_indicators(tweet) == " \nHere is my complete guide to crypto: "

def test_remove_tweet_statistics(): 
    tweet = "Very high inflation in 2022!\n4\n28k\n190"
    assert _remove_tweet_statistics(tweet) == "Very high inflation in 2022!"

def test_remove_date(): 
    tweet = "Today's date is 20 Mar 1999"
    assert _remove_tweet_date(tweet) == "Today's date is " 

    with pytest.raises(AssertionError): 
        tweet = "Today's date is 20 March 1999"
        assert _remove_tweet_date(tweet) == "Today's date is "

    with pytest.raises(AssertionError):
        tweet = "Today's date is Mar 20, 1999"
        assert _remove_tweet_date(tweet) == "Today's date is "

def test_clean_tweet(): 
    tweet = " Raphinha rejoindra le Bayern Munich pour un montant de 50 millions d'euros.\n\n \n@TNTSportsBR\n34\n491\n2,133"
    assert clean_tweet(tweet) == " Raphinha rejoindra le Bayern Munich pour un montant de 50 millions d'euros.  "

def test_tokenize(): 
    tweet = "Ce tweet est destinée à toutes les personnes voulant se lancer dans le commerce."
    tokens = ["ce" ,"tweet", "est", "destinée", "à", "toutes", "les", "personnes", "voulant", "se", "lancer", "dans", "le", "commerce", "."]
    assert tokenize(tweet) == tokens 

    with pytest.raises(AttributeError): 
        tokenize(["hello", "world"])

def test_remove_punctuation(): 

    sentence = ["hello", "world", "!"]
    assert remove_punctuation(sentence) == ["hello", "world"]

    sentence = ["!", ","]
    assert remove_punctuation(sentence) == []

    tweet = "I love #Python."
    assert remove_punctuation(tokenize(tweet)) == ["i", "love", "python"]

def test_remove_stopwords(): 
    text = "ce tweet est vraiment pertinent et bienveillant"
    tokens = tokenize(text)
    assert remove_stopwords(tokens) == ["tweet", "vraiment", "pertinent", "bienveillant"]

    text = "pas assez confiance en sa stratégie"
    assert remove_stopwords(tokenize(text)) == ["pas", "confiance", "stratégie"] 