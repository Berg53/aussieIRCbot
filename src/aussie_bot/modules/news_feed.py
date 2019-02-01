"""selecting news items from rss feeds"""
import logging

import feedparser


_LOGGER = logging.getLogger(__name__)


def newsfeed(num, newsoutlet):
    """News feed !n # #"""

    try:
        user_look_up = {
            "1": "https://abcnews.go.com/abcnews/technologyheadlines",
            "2": "https://abcnews.go.com/abcnews/internationalheadlines",
            "3": "https://abcnews.go.com/abcnews/topstories",
            "4": "https://www.news.com.au/content-feeds/latest-news-national",
            "5": "https://www.news.com.au/content-feeds/latest-news-world",
        }
        if int(newsoutlet) >= 6 or int(newsoutlet) <= 0:
            return "please number between 1 and 5 for the newsfeeds item !n - # . 1:technologyheadlines 2:internationalheadlines 3:topstories 4:latest-news-national 5: latest-news-world"
        print(num)
        if int(num) >= 11 or int(num) <= 0:
            return "please number between 1 and 10 for the news item !n # -"
        data_feed = feedparser.parse(user_look_up.get(newsoutlet))
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

        for index, entry in enumerate(data_feed["entries"]):
            news = entry["guid"]
            news1 = entry["summary"]
            if index >= int(num):
                print(num)
                break
        return "{} :URL = {}".format(news1, news)
    except Exception as error_name:
        _LOGGER.error("News Log errors %s", error_name)


def handler(connection, event):
    if event.arguments and event.arguments[0].startswith("!n"):
        args = event.arguments[0].split()

        try:
            if len(args) > 2:
                return connection.privmsg(event.target, newsfeed(*args[1:3]))
        except Exception as e:
            _LOGGER.warning(e)

        connection.privmsg(
            event.target,
            "Use the format !n num num the first is the news item and the second is the"
            " newsfeed. !n # #",
        )


def get_handlers():
    return (("pubmsg", handler),)
