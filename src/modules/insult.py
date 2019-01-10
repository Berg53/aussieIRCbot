import random
import os.path
import feedparser


def newsfeed(num, newsoutlet):
    try:
        USER_LOOKUP = {
        "1": "https://abcnews.go.com/abcnews/technologyheadlines",
        "2": "https://abcnews.go.com/abcnews/internationalheadlines",
        "3": "https://abcnews.go.com/abcnews/topstories",
        "4": "https://www.news.com.au/content-feeds/latest-news-national",
        "5": "https://www.news.com.au/content-feeds/latest-news-world",
        }
        #using a different keyword format#
        if int(newsoutlet) == 4 or int(newsoutlet) == 5:
            d = feedparser.parse(USER_LOOKUP.get(newsoutlet))
            for index, entry in enumerate(d['entries']):
                news = (entry['subtitle'])
                news1 = (entry['link'])
                if index >= int(num):
                    break 
            return("{} :URL = {}".format(news , news1))







        if not newsoutlet:
            newsoutlet = 1
        if int(newsoutlet) >= 4 or int(newsoutlet) <=0:
            return('please number between 1 and 5 for the newsfeeds item !n - # . 1:technologyheadlines 2:internationalheadlines 3:topstories 4:latest-news-national 5: latest-news-world')
            

        if int(num) >=int(11):
            return('please number between 0 and 10 for the news item !n # -')
        d = feedparser.parse(USER_LOOKUP.get(newsoutlet))
        for index, entry in enumerate(d['entries']):
            news = (entry['guid'])
            news1 = (entry['summary'])
            if index >= int(num):
                print(num)
                break 
        return("{} :URL = {}".format(news1 , news))
    except Exception as e:
        logger.error('News Log errors' , (e))


def random_line(insult_file=None):
    if insult_file is None:
        insult_file = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "data", "insult.txt"
        )
    with open(insult_file) as f:
        return random.choice(list(f))


def random_text(random_file=None):
    if random_file is None:
        random_file = os.path.join(
            os.path.dirname(os.path.dirname(__file__)), "data", "random.txt"
        )
    with open(random_file) as f:
        return random.choice(list(f))
