from bs4 import BeautifulSoup
import urllib3
import re

#list of sites visited
listmap = set("wiki/Baylor_University")

# scrape takes a url and gets a list of embedded urls from the html
# returns the number of files visited

def scrape(url, counter):

    #get GET request page
    response = http.request('GET', url)

    #get html from request responce
    soup = BeautifulSoup(response.data, features="html5lib")

    #write the current URL to the document
    f.write(url + "\t")

    #for each link found within the html
    for link in soup.findAll('a', attrs={'href': re.compile("^/wiki/[a-zA-z-0-9_()-]+$")}):

        #parse the href to get the link
        currentUrl = link.get('href')

        #print the found link
        print(currentUrl)

        #write it to a file
        f.write(currentUrl + "\t")

        #increment the counter
        counter = counter + 1

        #we dont want to go overboard
        if counter < 1000:
            #if we have not visited the link before
            if currentUrl in listmap:
                print("duplicate")
            else:
                #add the current node to the list
                listmap.add(currentUrl)

                #write to the file
                f.write("\n")

                #scrape on that node
                counter = scrape(baseUrl + link.get('href'), counter)

    f.write("\n")
    return counter

#counter for number of files
counter = 0;

#empty the dataset
open("dataset", 'w').close()

#open the file
f = open("dataset", "a")

#init database link
http = urllib3.PoolManager()

#base link url
baseUrl = "https://en.wikipedia.org"

#starting node
url = 'https://en.wikipedia.org/wiki/Baylor_University'

#count the number of sites added
counter = scrape(url, counter)

print(counter)

