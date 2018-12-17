from urllib import urlopen

from BeautifulSoup import BeautifulSoup

import re
def gettitle(url):
    urltext = re.search("(?P<url>https?://[^\s]+)", url).group("url")
        
    print urltext
    # Copy all of the content from the provided web page
    webpage = urlopen(url).read()

    # Grab everything that lies between the title tags using a REGEX
    patFinderTitle = re.compile('')


    soup2 = BeautifulSoup(webpage)

    #print soup2.findAll("title")

    titleSoup = soup2.findAll("title")

    descSoup = soup2.findAll("p")
    titleSoup = str(titleSoup).strip('[<title>')
    titleSoup = titleSoup.replace('&#39;', "'")
    titleSoup = titleSoup.strip('</title>]')

    return titleSoup 

print gettitle('https://www.abc.net.au/news/2018-12-17/diwan-al-dawla-charity-status-revoked/10626908')
