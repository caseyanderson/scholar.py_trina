## cleanup

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
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
    numChunks = int(chunk)
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
