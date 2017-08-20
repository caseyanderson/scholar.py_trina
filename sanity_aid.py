# make the dictionary

def makeDictionary(source, g_field):
    entries = list( {} for i in source)
    key = str(g_field)
    for i in source:
        entries[key] = i[1]
    return entries




## convert all of second layer

secondlayerDicts = [[{} for i in range(10)] for j in range(10)]

for h, i in enumerate( secondlayerCitations ):
    for k,j in enumerate(i):
        secondlayerDicts[h][k]['citations']=j[1]
        secondlayerDicts[h][k]['citations list']=j[2]


###

secondlayerDicts_chunk = secondlayerDicts[4:6]

thirdlayerHTML4 = [['' for i in range(10)] for j in range(10)]

for h,i in enumerate(secondlayerDicts_chunk):
    for j,k in enumerate(i):
        print(''.join(['step number ', str(j), '\n', str(k['citations list']), '\n','\n']))
        thirdlayerHTML4[h][j] = google2soup(k['citations list'])
        print('wait for 5')
        sleep(5)
    print('wait for 20')
    sleep(20)


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


for i in article:
    author_00 = list()
    title_00 = list()
    year_00 = list()
    citation_00 = list()
    excerpt_00 = list()

    author_00.append(parseArticleResultField(i, 'author'))
    title_00.append(parseArticleResultField(i, 'title'))
    year_00.append(parseArticleResultField(i, 'year'))
    citation_00.append(parseArticleResultField(i, 'citations'))
    excerpt_00.append(parseArticleResultField(i, 'excerpt'))
