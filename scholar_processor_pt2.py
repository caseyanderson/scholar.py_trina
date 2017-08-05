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
            sleep(4)
            second_layer_results[h].append(a)
    else:
        second_layer_results[h] = ''




### parse and combine with separated entries below, this was just a test

for h, i in enumerate(second_layer_results[0]):
    if i != '':
        print(''.join(['step ', str(h), '\n', '\n', str(i), '\n', '\n']))
        sleep(4)


## gets all titles from second layer, done

title_stash = x = [['' for i in range(1)] for j in range(10)]

for h, i in enumerate(second_layer_results):
    if i != '':
        for x in i:
            if x != '':
                for a in x.find_all('h3', class_= 'gs_rt'):
                    for y in a.find_all('a'):
                        print(''.join(['2nd layer result number ', str(h), '\n', '\n', str(y.contents), '\n', '\n' ]))
                        title_stash[h].append(y.contents)
                        sleep(1)


## get all citation numbers, done

citation_stash = x = [['' for i in range(1)] for j in range(10)]

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

## get all citation urls, done

url_stash = x = [['' for i in range(1)] for j in range(10)]

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

## gets all authors and year from second layer

author_year_stash = x = [['' for i in range(1)] for j in range(10)]

for h, i in enumerate(second_layer_results):
    if i != '':
        for x in i:
            if x != '':
                for a in x.find_all('div', class_='gs_a'):
                    #print(''.join(['2nd layer result number ', str(h), '\n', '\n', str(a.contents), '\n', '\n']))
                    author_year_stash[h].append(a.contents)

## dear lord this one is tough...gotta split this up and write to a text file, manually fix author names, and then bring back into python

outputFile = '/Users/mdp/git/scholar.py_trina/author_fix.txt'

thefile = open(outputFile, 'w')

for h, i in enumerate(author_year_stash):
    if i != '':
        for x in i:
            for e in x:
                blah = ''.join(e)
                splits = blah.split(' - ')
                for a in splits:
                    if isinstance(a, str) is False:
                        out = ''.join([str(h), '\n', str(a.contents), '\n','\n'])
                        thefile.write(out)
                    else:
                        out = ''.join([str(h), '\n', str(a), '\n','\n'])
                        thefile.write(out)

thefile.close()


# authors = x = [['' for i in range(1)] for j in range(10)]
