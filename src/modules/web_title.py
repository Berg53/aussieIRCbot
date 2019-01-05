import re
from urllib.request import urlopen

from logger import logger
from bs4 import BeautifulSoup


def gettitle(url, user):
    print(url)
    urlsplit = url.split(".")
    num=len(urlsplit)
    try:
        if urlsplit[num - 1] == "iso": 
            return'Fuck off with your downloads ' + user
    except:
        pass
    # Copy all of the content from the provided web page
    webpage = urlopen(url).read()

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
