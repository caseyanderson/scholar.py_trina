# make the dictionary

entries = list( {} for i in author_00)

def makeDictionary(source, g_field, output):
    key = str(g_field)
    for h,i in enumerate(source):
        output[h][key] = i[1]
    return output




## convert all of second layer

secondlayerDicts = [[{} for i in range(10)] for j in range(10)]

for h, i in enumerate( secondlayerCitations ):
    for k,j in enumerate(i):
        secondlayerDicts[h][k]['citations']=j[1]
        secondlayerDicts[h][k]['citations list']=j[2]


###

secondlayerDicts_chunk = secondlayerDicts[0:2]

thirdlayerHTML_testing = [['' for i in range(10)] for j in range(10)]

for h,i in enumerate(secondlayerDicts_chunk):
    for j,k in enumerate(i):
        print(''.join(['step number ', str(j), '\n', str(k['citations list']), '\n','\n']))
        # thirdlayerHTML4[h][j] = google2soup(k['citations list'])
        print('wait for 5')
        # sleep(5)
    print('wait for 20')
    # sleep(20)


## parse third layers

In [449]: thirdlayer00 = thirdlayerHTML[0][0]
In [449]: thirdlayer00articles = parseArticles(thirdlayer00)
 for h,i in enumerate(thirdlayer00articles):
     ...:     print(''.join(['step number ', str(h), '\n', str(i), '\n', '\n' ]))
     ...:     sleep(2)
     ...:

In [449]: thirdlayer00articles_clean = eliminateEdges(thirdlayer00articles)


thirdlayerProcessed = [[{} for i in range(10)] for j in range(4)]
fields = ['title', 'author', 'year', 'citations', 'excerpt']

article0 thir['' for i in range(10)]
