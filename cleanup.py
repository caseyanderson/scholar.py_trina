## parsing google scholar

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
from time import sleep


## read a file at path and return contents of the file
def readfile(path):
    f = open(str(path), 'r')
    results = f.read()
    return results


## write contents of list (data) to a file at path
def writeFile(path, data):
    outputFile = str(path)
    thefile = open(outputFile, 'w')
    data = list(data)

    for i in data:
        out = ''.join([ str(i), '\n' ])
        thefile.write(out)

    thefile.close()


## outputs a list of a number sequence from start to end
def num_sequence(start, end):
    x = list(range(start, end))
    return x


## takes a list (content) and divides it into sublists of size chunk (num)
def chunks(content, num):
    data = list(content)
    numChunks = int(num)
    processed = [data[x:x+numChunks] for x in range(0, len(data), numChunks)]
    return list(processed)


## takes a list (data) and strips leading and trailing whitespace from each item
def stripWS(data):
    info = list(data)

    for h,i in enumerate(info):
        i = i.strip()
        info[h] = i

    return info


## request something from google, put it in a soup object
def google2soup(link):
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    return soup


## basic pattern for looking at soup results by category:
def searchResultCategory(data):
    for h, i in enumerate(data):
        if h == 0:
            output = list()
            ## do the stuff
            output.append(i)
        else:
            ## do the stuff
            output.append(i)
    return output


## takes a soup object as input and returns first ten google scholar result articles, can be reused on subsequent pages to get more results

def parseArticles(data):
    results = data.find_all('div', class_='gs_r')
    return results

# scholar_fields = ['Title', 'Author', 'URL', 'Year', 'Citations', 'Citations list', 'Excerpt']


def parseArticleResultField(data, g_field):
    g_field = str(g_field)
    results = list()
    if data != list:
        data = list(data)

        for x in data:  # i probably need to make something that skips the results that break the code...look for [Citation]
            if x != '':
                if g_field == 'title':
                    for a in x.find_all('h3', class_='gs_rt'):
                        for y in a.find_all('a'):
                            title = y.get_text()
                            results.append(title)
                # author goes here
                elif g_field == 'year':
                    for a in x.find_all('div', class_='gs_a'):
                        blah = a.get_text()
                        year = re.search(r"(\d{4})", blah).group(1)
                        results.append(year)
                elif g_field == 'excerpt':
                    for a in x.find_all('div', class_='gs_rs'):
                        url = a.get_text()
                        results.append(url)
                # elif g_field == 'author':
                #     for a in x.find_all('div', class_='gs_a'):
                #             blah = a.get_text()
                #             blah = blah.split(' - ')
                #             results.append(blah)
            else:
                results.append('n/a')

        return results
