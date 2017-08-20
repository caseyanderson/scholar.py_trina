## making third layers
import random

## get second layer from txt file (see formatted_data python files)



parsed = [['' for i in range(10)] for j in range(10)]

for h, i in enumerate(secondlayerDicts[9:]):
    for j, k in enumerate(i):
        print(''.join([ 'second layer article number ', str(j), '\n', k['citations list'], '\n', '\n' ]))
        url = k['citations list']
        soup = google2soup(url)
        sleep(random.uniform(20, 60))
        path = ''.join([ '/Users/mdp/git/trina_data/formatted_data_v1/layer_3/pos9/result', str(j), '.py'])
        writeFile(path, soup)


###

## write contents of list (data) to a file at path
def writeFile(path, data):
    outputFile = str(path)
    thefile = open(outputFile, 'w')
    data = list(data)

    for i in data:
        out = ''.join([ str(i), ',', '\n' ])
        thefile.write(out)

    thefile.close()
