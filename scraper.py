from bs4 import BeautifulSoup
import urllib3
import re

counter = 0

listmap = set("wiki/Baylor_University")

def scrape(url, counter):
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data, features="html5lib")

    f.write(url + "\t")
    for link in soup.findAll('a', attrs={'href': re.compile("^/wiki/[a-zA-z-0-9_()-]+$")}):
        currentUrl = link.get('href')
        print(currentUrl)
        f.write(currentUrl + "\t")
        counter = counter + 1
        if counter < 1000:
            if currentUrl in listmap:
                print("duplicate")
            else:
                listmap.add(currentUrl)
                f.write("\n")
                counter = scrape(baseUrl + link.get('href'), counter)

    f.write("\n")
    return counter



open("dataset", 'w').close()
f = open("dataset", "a")

http = urllib3.PoolManager()

baseUrl = "https://en.wikipedia.org"

url = 'https://en.wikipedia.org/wiki/Baylor_University'

counter = scrape(url, counter)

print(counter)

