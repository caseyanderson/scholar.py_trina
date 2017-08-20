## making third layers
import random

## get second layer from txt file

parsed = [['' for i in range(10)] for j in range(10)]

for h, i in enumerate(secondlayerDicts[:1]):
    print(''.join([ 'second layer article number ', str(h), '\n', i['citations list'], '\n', '\n' ]))
    url = i['citations list']
    soup = google2soup(url)
    sleep(random.randint(5, 10))
    parse = list()
    parse = parseArticles(soup)
    sleep(1)


thirdlayer2request = [ ]
