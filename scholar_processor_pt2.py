'''
scholar_processor.py pt. 2

getting the nested citation lists...

'''

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from time import sleep


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
        sleep(4) ## i end up with 11 if i remove this?
    else:
        # print(''.join(['No citation', ' at position ', str(num), '\n']))
        second_layer.append('')


## storing second layer results here for processing after making a this

second_layer_results = x = [['' for i in range(1)] for j in range(10)]


## if the second layer is empty for a list item that means that that article should have 0 citations

for h, i in enumerate(second_layer): # for each url
    # print(' '.join(['article number', str(h), '\n']))
    # print()
    # print()
    if i != '':
        for a in i.find_all('div', class_='gs_r'):
            print(''.join([str(a), '\n', '\n']))
            # sleep(4)
            second_layer_results[h].append(a)
    else:
        second_layer_results[h] = ''




############### below is broken

        for j in i:
            for a in j.find_all('div', class_='gs_r'): # get each entry (max 10)
                print(' '.join(['entry number', str(num), '\n']))
                second_layer_results[h].append(j)
    else:
        second_layer_results[h] = ''

            # print(info)
            # print()
            # print()
            # sleep(2)
