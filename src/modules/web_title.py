import re
from urllib.request import urlopen
import requests
from logger import logger
from bs4 import BeautifulSoup


def gettitle(url, user):
    print(test)
    testUrl=requests.get(url, stream=True)
    (testUrl.headers['Content-Type']) = (testUrl.headers['Content-Type']).lstrip()
    print(testUrl.headers['Content-Type'])
    try:
        if (testUrl.headers['Content-Type'].find()) != "text/html": 
            #text/html;charset=utf-8
            return'Fuck off with your downloads ' + user + (testUrl.headers['Content-Type'])
    except:
        pass
    # Copy all of the content from the provided web page
    webpage = urlopen(url).read()
    testUrl=requests.get(url, stream=True)
    print(testUrl)

    # Grab everything that lies between the title tags using a REGEX
    patFinderTitle = re.compile("")

    soup2 = BeautifulSoup(webpage, features="html.parser")
    titleSoup = soup2.findAll("title")
    descSoup = soup2.findAll("p")
    titleSoup = str(titleSoup).strip("[<title>")
    titleSoup = titleSoup.strip("</title>]")
    titleSoup = re.sub("&#(\d+);", lambda m: chr(int(m.group(1))), titleSoup)
    titleSoup = titleSoup.lstrip()
    logger.info(titleSoup)
    print(titleSoup)
    return(titleSoup)
