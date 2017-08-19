# make the dictionary

def makeDictionary(source, g_field):
    entries = list( {} for i in source)
    key = str(g_field)
    for i in source:
        entries[key] = i[1]
    return entries




## convert all of second layer

secondlayerArticles = list()

for i in seclayer:
    convert = parseArticles(i)
    sleep(1)
    for j in convert:
