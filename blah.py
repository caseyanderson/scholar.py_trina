## i dont believe i have to do this as long as i sleep for at least 4 seconds in between requests to google scholar


outputFile = '/Users/mdp/git/scholar.py_trina/second_layer_stash.txt'


thefile = open(outputFile, 'w')

for i in second_layer:
    out = ''.join([ str(i), '\n', '\n' ])
    thefile.write(out)

thefile.close()

####

## import stupid manual author file and deal with it a la the below this was annoying but figured out some cool things (chunks etc)

inputFile = '/Users/mdp/git/scholar.py_trina/author_fix.txt'

thefile = open(inputFile, 'r')

with open(inputFile) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

content = list(filter(None, content)) # fastest

## get rid of second number
for x, y in enumerate(content):
    content[(x*3)] = content[(x*3)][:1]

## divide into chunks
chunks = [content[x:x+num] for x in range(0, len(content), num)]

## now that this is in chunks, look at first item of each chunk to get entry number

clean_author_stash = x = [['' for i in range(1)] for j in range(10)]

for i in chunks:
    if i != '':
        step = int(i[0])
        author = i[1]
        clean_author_stash[step].append(author)

clean_year_stash = x = [['' for i in range(1)] for j in range(10)]

for i in chunks:
    if i != '':
        step = int(i[0])
        year = i[2]
        clean_year_stash[step].append(year)

thefile.close() ## closing the file

## the rest of the processing for above is over with everything else in scholar_processor_pt2.py

#######

## dataset draft 1:


outputFile = '/Users/mdp/git/scholar.py_trina/dataset08062017.txt'


thefile = open(outputFile, 'w')

for i in separated_entries:
    out = ''.join([ str(i), '\n', '\n' ])
    thefile.write(out)
#    print(out)
#    sleep(4)

thefile.close()
