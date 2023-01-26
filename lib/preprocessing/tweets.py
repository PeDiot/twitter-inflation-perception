"""Description. Remove polluting features in tweets: mentions, links, retweets, etc."""

import string 
import re

from typing import List 

MENTION = "@[A-Za-z0-9_]+"
DATE = "[\s]\d{2}[^\S\n\t]+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)+[\s]\d{4}"

def _remove_mentions(tweet: str) -> str: 
    """Description. Remove all mentions in tweets containing the @ flag."""

    return re.sub(MENTION,"", tweet)

def _remove_links(tweet: str) -> str: 
    """Description. Remove all links in tweets."""

    tweet = re.sub(r"http\S+", "", tweet)
    tweet = re.sub(r"www.\S+", "", tweet)
    return tweet 

def _remove_tweet_indicators(tweet: str) -> str: 
    """Description. Remove Twitter indicators such as thread or replies."""

    for indicator in ("Show this thread", "Replying to"): 
        tweet = tweet.replace(indicator, "")
    return tweet

def _remove_tweet_statistics(tweet: str) -> str: 
    """Description. 
    Remove number of retweets, likes and comments at the end of the text."""

    lines = [
        line 
        for line in tweet.splitlines()
        if len(line.split(" ")) > 1 and line.isdigit() == False
    ]
    return " ".join(lines)

def _remove_tweet_date(tweet: str) -> str: 
    """Description. Remove date in for tweet replies.
    
    Details: date format is always %d %b %YYYY"""

    return re.sub(DATE, " ", tweet)


def clean_tweet(tweet: str, remove_mentions: bool=True) -> str: 
    """Description. 
    Remove mentions, links, thread indicator and statistics from tweet."""

    funs = [_remove_links, _remove_mentions, _remove_tweet_indicators, _remove_tweet_statistics, _remove_tweet_date]
    
    if not remove_mentions: 
        funs.remove(_remove_mentions)

    for f in funs: 
        tweet = f(tweet)

    return tweet