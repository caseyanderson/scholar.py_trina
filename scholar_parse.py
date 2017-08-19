'''
parsing google scholar results

fields we care about: 'Title', 'Author', 'Year', 'Citations', 'Citations list', 'Excerpt'

'''

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


## request something from google, put it in a soup object
def google2soup(link):
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    return soup


## takes a soup object as input and returns first ten google scholar result articles, can be reused on subsequent pages to get more results

def parseArticles(data):
    results = data.find_all('div', class_='gs_r')
    return results

## eliminates articles that break my parseArticleResultField below
# sometimes i have to run this twice, no idea why

def eliminateEdges(data):
    for h,i in enumerate(data):
        if i is None:
            print("None")
        else:
            for a in i.find_all('span', class_='gs_ct1'):
                if a is not None:
                    if '[CITATION]' in a.get_text():
                        # print(a.get_text())
                        data.pop(h)
    return data


def parseArticleResultField(data, g_field):
    g_field = str(g_field)
    results = list()
    if data != list:
        data = list(data)

        for n,x in enumerate(data):
            if x != '':
                if g_field == 'title':
                    for a in x.find_all('h3', class_='gs_rt'):
                        for y in a.find_all('a'):
                            title = y.get_text()
                            results.append(title)
                elif g_field == 'author':
                    for a in x.find_all('div', class_='gs_a'):
                        author = a.get_text()
                        clean = author.split(' - ')
                        author = clean[0]
                        results.append(author)
                elif g_field == 'year':
                    for a in x.find_all('div', class_='gs_a'):
                        blah = a.get_text()
                        year = re.search(r"(\d{4})", blah).group(1)
                        results.append(year)
                elif g_field == 'citations':
                    for j, a in enumerate(x.find_all('div', class_='gs_fl')):
                        if a != None:
                            for y in a.find('a', attrs = { 'href' : True }):
                                if 'Cited by' in y:
                                    cited = y
                                    num = cited.split(' ')
                                    num[2] = int(num[2])
                                    if num[2] != 0:
                                        url = a.find('a')['href']
                                        url = ''.join(['https://scholar.google.com', url])
                                        results.append([cited, url, n]) # added n here as a hack to fix sync issues
                elif g_field == 'excerpt':
                    for a in x.find_all('div', class_='gs_rs'):
                        excerpt = a.get_text()
                        results.append(excerpt)
            else:
                results.append('n/a')

        return results

#########
## basic cleanup stuff used in earlier versions of this
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
