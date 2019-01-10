#!/usr/bin/env python
# -*- coding: utf-8; mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vim: fileencoding=utf-8 tabstop=4 expandtab shiftwidth=4

import re
from urllib.request import urlopen
import requests
from logger import logger
from bs4 import BeautifulSoup


def gettitle(url, user):
    testUrl=requests.get(url, stream=True)
    print(testUrl)
    htmlcontent = (testUrl.headers['Content-Type'])
    print(htmlcontent)
    try:

        if (htmlcontent.find('text/html')) == -1:
            print("debug")
            return'Fuck off with your downloads ' + user
    except Exception as e:
        print(e)
        pass
    # Copy all of the content from the provided web page
    webpage = urlopen(url).read()


    # Grab everything that lies between the title tags using a REGEX
    patFinderTitle = re.compile("")

    soup2 = BeautifulSoup(webpage, features="html.parser")
    titleSoup = soup2.findAll("title")
    titleSoup = str(titleSoup).strip("[<title>")
    titleSoup = titleSoup.strip("</title>]")
    titleSoup = re.sub("&#(\d+);", lambda m: chr(int(m.group(1))), titleSoup)
    titleSoup = titleSoup.lstrip()
    logger.info(titleSoup)
    print(titleSoup)
    return("{} {}" . format(titleSoup, url))
