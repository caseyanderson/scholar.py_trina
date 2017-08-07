## cleanup

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from time import sleep

## read a file at path and return contents of the file
def readfile(path):
    f = open(str(path), 'r')
    results = f.read()
    return results


## write contents (data) to a file at path
def writeFile(path, data):
    outputFile = str(path)
    thefile = open(outputFile, 'w')
    data = list(data)

    for i in data:
        out = ''.join([ str(i), '\n', '\n' ])
        thefile.write(out)

    thefile.close()


def num_sequence(start, end):
    x = list(range(start, end))
    return x


## takes a list (content) and divides it into sublists of size chunk (num)
def chunks(content, num):
    data = list(content)
    numChunks = int(chunk)
    processed = [data[x:x+numChunks] for x in range(0, len(data), numChunks)]
    return list(processed)


## request something from google, put it in a soup object
def google2soup(link):
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    return soup
