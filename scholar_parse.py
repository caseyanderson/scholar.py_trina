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

## eliminates articles that break my parseArticleResultField below

def eliminateEdges(data):
    for h,i in enumerate(data):
        for a in i.find_all('span', class_='gs_ct1'):
            if a is not None:
                if '[CITATION]' in a.get_text():
                    data.pop(h)
    return data


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
                elif g_field == 'citations':
                    for a in x.find_all('div', class_='gs_fl'):
                        for y in a.find('a'):
                            if 'Cited' in y:
                                cited = y
                                num = cited.split(' ')
                                num[2] = int(num[2])
                                if num[2] != 0:
                                    url = a.find('a')['href']
                                    url = ''.join(['https://scholar.google.com', url])
                                    results.append([cited, url])
                                else:
                                    cited = 0
                                    url = 'n/a'
                                    results.append([cited, url])
                elif g_field == 'excerpt':
                    for a in x.find_all('div', class_='gs_rs'):
                        excerpt = a.get_text()
                        results.append(excerpt)
            else:
                results.append('n/a')

        return results




for h, i in enumerate(second_layer_results):
    if i != '':
        for x in i:
            if x != '':
                for a in x.find_all('div', class_='gs_fl'):
                    link = a.find('a')['href']
                    if 'cites' in link:
#                        print(link)
                        # print(''.join(['2nd layer result number ', str(h), '\n', '\n', str(link), '\n', '\n']))
                        url_stash[h].append(link)
                        sleep(1)
                    else:
                        print('skip!')


for h, i in enumerate(second_layer_results):
    if i != '':
        for x in i:
            if x != '':
                for a in x.find_all('div', class_='gs_fl'):
                    for y in a.find('a'):
                        if 'Cited' in y:
                            print(''.join(['2nd layer result number ', str(h), '\n', '\n', str(y), '\n', '\n']))    # i should be able to get the citation url here too i think
                            citation_stash[h].append(y)
                            sleep(2)
