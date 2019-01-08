import random
import os.path
import feedparser


def newsfeed(num, newsoutlet):
    USER_LOOKUP = {
    "1": "https://abcnews.go.com/abcnews/technologyheadlines",
    "2": "https://abcnews.go.com/abcnews/internationalheadlines",
    "3": "https://abcnews.go.com/abcnews/topstories",
    }
    if not newsoutlet:
        newsoutlet = 1
    if int(newsoutlet) >= 4 or int(newsoutlet) <=0:
        return('please number between 1 and 3 for the newsfeeds item !n - # . 1:technologyheadlines 2:internationalheadlines 3:topstories')
        

    if int(num) >=int(11):
        return('please number between 0 and 10 for the news item !n # -')
    d = feedparser.parse(USER_LOOKUP.get(newsoutlet))
    for index, entry in enumerate(d['entries']):

        news = (entry['guid'])
        news1 = (entry['summary'])
        print(index)
        if index >= int(num):
            print(num)
            break 
    return("{} :URL = {}".format(news1 , news))
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
