'''selecting news items from rss feeds'''
import random
import os.path
import feedparser
from logger import LOGGER




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
