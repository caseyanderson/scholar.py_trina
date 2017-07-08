'''
scholar_processor.py pt. 2

getting the nested citation lists...

'''

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


def google2soup(link):
    req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    return soup
