## i dont believe i have to do this as long as i sleep for at least 4 seconds in between requests to google scholar


outputFile = '/Users/mdp/git/scholar.py_trina/second_layer_stash.txt'


thefile = open(outputFile, 'w')

for i in second_layer:
    out = ''.join([ str(i), '\n', '\n' ])
    thefile.write(out)

thefile.close()
