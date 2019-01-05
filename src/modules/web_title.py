import re
from urllib.request import urlopen

from logger import logger
from bs4 import BeautifulSoup


def gettitle(url):
    print(url)
    # Copy all of the content from the provided web page
    webpage = urlopen(url, timeout=10).read()

    # Grab everything that lies between the title tags using a REGEX
    patFinderTitle = re.compile("")

    soup2 = BeautifulSoup(webpage, features="html.parser")
    titleSoup = soup2.findAll("title")
    descSoup = soup2.findAll("p")
    titleSoup = str(titleSoup).strip("[<title>")
    titleSoup = titleSoup.strip("</title>]")
    titleSoup = re.sub("&#(\d+);", lambda m: chr(int(m.group(1))), titleSoup)
    logger.info(titleSoup)
    print(titleSoup)
    return titleSoup
