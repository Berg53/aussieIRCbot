#!/usr/bin/env python
# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# gedit: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4
'''Define the title of web pages in irc'''
import re
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
from logger import LOGGER


def gettitle(url, user):
    '''find the title of a url address'''
    test_url = requests.get(url, stream=True)
    print(test_url)
    htmlcontent = test_url.headers["Content-Type"]
    print(htmlcontent)
    try:

        if (htmlcontent.find("text/html")) == -1:
            print("debug")
            return "Fuck off with your downloads " + user
    except Exception as error_message:
        print(error_message)
    # Copy all of the content from the provided web page
    webpage = urlopen(url).read()

    # Grab everything that lies between the title tags using a REGEX

    soup2 = BeautifulSoup(webpage, features="html.parser")
    title_soup = soup2.findAll("title")
    title_soup = str(title_soup).strip("[<title>")
    title_soup = title_soup.strip("</title>]")
    title_soup = re.sub(r"&#(\d+);", lambda m: chr(int(m.group(1))), title_soup)
    title_soup = title_soup.lstrip()
    LOGGER.info(title_soup)
    print(title_soup)
    return "{} {}".format(title_soup, url)
