'''selecting news items from rss feeds'''
import random
import os.path
import feedparser
from logger import logger


def newsfeed(num, newsoutlet):
    '''News feed !n # #'''
    try:
        user_look_up = {
            "1": "https://abcnews.go.com/abcnews/technologyheadlines",
            "2": "https://abcnews.go.com/abcnews/internationalheadlines",
            "3": "https://abcnews.go.com/abcnews/topstories",
            "4": "https://www.news.com.au/content-feeds/latest-news-national",
            "5": "https://www.news.com.au/content-feeds/latest-news-world",
        }
        # using a different keyword format#
        if int(newsoutlet) == 4 or int(newsoutlet) == 5:
            data_feed = feedparser.parse(user_look_up.get(newsoutlet))
            for index, entry in enumerate(data_feed["entries"]):
                news = entry["subtitle"]
                news1 = entry["link"]
                if index >= int(num):
                    break
            return "{} :URL = {}".format(news, news1)

        if not newsoutlet:
            newsoutlet = 1
        if int(newsoutlet) >= 4 or int(newsoutlet) <= 0:
            return "please number between 1 and 5 for the newsfeeds item !n - # . 1:technologyheadlines 2:internationalheadlines 3:topstories 4:latest-news-national 5: latest-news-world"

        if int(num) >= int(11):
            return "please number between 0 and 10 for the news item !n # -"
        data_feed = feedparser.parse(user_look_up.get(newsoutlet))
        for index, entry in enumerate(data_feed["entries"]):
            news = entry["guid"]
            news1 = entry["summary"]
            if index >= int(num):
                print(num)
                break
        return "{} :URL = {}".format(news1, news)
    except Exception as error_name:
        logger.error("News Log errors %s", (error_name))


def random_line(insult_file=None):
    '''to insult users all day'''
    if insult_file is None:
        insult_file = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "data", "insult.txt"
        )
    with open(insult_file) as file_used:
        return random.choice(list(file_used))


def random_text(random_file=None):
    '''Random selective quotes from file'''
    if random_file is None:
        random_file = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "data", "random.txt"
        )
    with open(random_file) as file_used:
        return random.choice(list(file_used))
