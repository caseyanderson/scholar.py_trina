# make the dictionary

def makeDictionary(source, g_field):
    entries = list( {} for i in source)
    key = str(g_field)
    for i in source:
        entries[key] = i[1]
    return entries
