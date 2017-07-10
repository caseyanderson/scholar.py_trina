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


####
second_layer=[]

## gets second layer entries from citation lists per article, leaves an empty string for articles that are not cited

for num, info in enumerate(separated_entries):
    # first get each citation list per article
    cit_num = int(info['Citations'])
    if cit_num != 0:     # if citations are 0 there is no citations list
        # if there is a citation number, get the url from citations list and make a new soup object
        url = info['Citations list']
        second_layer.append(google2soup(url))
        sleep(2)
    else:
        print(''.join(['No citation', ' at position ', str(num), '\n']))
        second_layer.append('')


 ## breaks apart each citation list

for h, i in enumerate(second_layer): # for each url
    print(' '.join(['article number', str(h), '\n']))
    print()
    print()
    if i != '':
        for num, info in enumerate(i.find_all('div', class_='gs_r')): # get each entry (max 10)
            print(' '.join(['entry number', str(num), '\n']))
            print(info)
            print()
            print()
            sleep(2)
