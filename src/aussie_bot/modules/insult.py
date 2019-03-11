"""selecting news items from rss feeds"""
import random
import os.path
import re



INSULTS_LOCATION = os.getenv('INSULT_FILE', '/home/berg/bin/aussieIRCbot/src/aussie_bot/data/insult.txt')

def _get_insult():
    with open(INSULTS_LOCATION) as f:
        insults = f.readlines()
    return random.choice(insults)

def run(name):
    m = '{}, {}'.format(name,  _get_insult().lower())

    return m.strip()



def handler(connection, event):
    try:
        text = event.arguments[0].split()
    except:
        return
    if len(text) == 2 and event.arguments and text[0] == "!i":
        connection.privmsg(event.target, str(run(text[1])))
    if len(text) == 1 and event.arguments and text[0] == "!i": 
        connection.privmsg(event.target, _get_insult().strip())


def get_handlers():
    return (("pubmsg", handler),)
