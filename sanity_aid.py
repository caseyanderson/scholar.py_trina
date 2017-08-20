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
