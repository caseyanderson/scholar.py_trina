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


with open('outputs.txt', 'a') as outputs:
    baseDir = '/Users/mdp/git/trina_data/formatted_data_v1/layer_3/pos2/done/'

    listoffiles = ['result0.py',  'result1.py',  'result2.py',  'result3.py',  'result4.py',  'result5.py',  'result6.py',  'result7.py',  'result8.py',  'result9.py']


    for h,i in enumerate(listoffiles):
        print(''.join(['\n', '\n', '\n', 'list number ', str(h)]))
        path = ''.join([baseDir, i])
        f  = open(path, 'r')
        result = f.read()
        soup = BeautifulSoup(result, 'html.parser')
        f.close()
        articles = parseArticles(soup)
        test = [{} for i in range(10)]

        for j, k in enumerate(articles):
            print(''.join([ '\n', '\n', 'article number ', str(j)]))
            title = parseArticleResultField(k, 'title')
            author = parseArticleResultField(k, 'author')
            year =  parseArticleResultField(k, 'year')
            excerpt = parseArticleResultField(k, 'excerpt')
            citation = parseArticleResultField(k, 'citations')

            for l, m in enumerate(title):
                print(''.join(['title ', str(title[0][1])]))
                print(''.join(['author ', str(author[0][1])]))
                print(''.join(['year ', str(year[0][1])]))
                print(''.join(['excerpt ', str(excerpt[0][1])]))
                print(''.join(['citations ', str(citation[0][1])]))
                print(''.join(['citation list ', str(citation[0][2])]))
