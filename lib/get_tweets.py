"""Description. 

Retrieve tweets for inflation-related keywords using Scweet library.
"""

from Scweet.scweet import scrape

from .enums import (
    ECONOMICAL_TERMS, 
    PRICES, 
    EXPENSIVE,
    CHEAP, 
    INSTITUTIONS, 
    ENGLISH, 
    BACKUP, 
    CONFIG,
)

from rich import print
import os

def run(
    lexical_field: str, 
    start_date: str, 
    end_date: str, 
    lang: str="fr", 
    remove_replies: bool=True): 
    """Description. 
    
    Run Twitter scraping using Scweet scrape function.

    Attributes: 
        - lexical_field: lexical field of keywords to scrape
        - start_date: from which date
        - end_date: until which date 
        - lang: language of collected tweets
        - remove_replies: whether removing tweet replies

    Returns: collected data is stored as csv file into backup/tweets/

    Example: 
    >>> from lib import get_tweets

    >>> get_tweets.run(lexical_field="ECONOMICAL_TERMS", start_date="2022-01-01", end_date="2022-12-31")
    Scraping on headless mode.

    DevTools listening on ws://127.0.0.1:62870/devtools/browser/fb9f8ab3-45be-4cd4-a6fa-eae08f3fb3ed
    looking for tweets between 2022-01-01 and 2022-01-02 ...
    path : https://twitter.com/search?q=(inflation%20OR%20deflation%20OR%20stagflation%20OR%20desinflation%20OR%20inflationniste%20OR%20deflationniste%20OR%20antiinflationniste%20OR%20antideflationniste%20OR%20IPC%20OR%20IPCH)%20until%3A2022-01-02%20since%3A2022-01-01%20lang%3Afr%20-filter%3Areplies&src=typed_query
    scroll  1
    Tweet made at: 2022-01-01T17:33:07.000Z is found.
    Tweet made at: 2022-01-01T16:52:30.000Z is found.
    ...
    """

    _keys = list(CONFIG.keys())
    if lexical_field not in _keys: 
        raise ValueError(f"lexical field must be in {_keys}")

    if not os.path.isdir(BACKUP): 
        os.makedirs(BACKUP)

    data = scrape(
        words=CONFIG[lexical_field]["keywords"], 
        since=start_date, 
        until=end_date, 
        interval=1, 
        lang=lang,
        limit=CONFIG[lexical_field]["max_tweets"], 
        filter_replies=True, 
        save_dir=BACKUP, 
        file_name=CONFIG[lexical_field]["file_name"])

    n_tweets = data.shape[0]
    print(f"{n_tweets} collected tweets.")