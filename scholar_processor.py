'''
usage:

1. pipe output of scholar.py query into a text file

python3 scholar.py --phrase "digital_humanities" > "$(date +"%Y_%m_%d_%I_%M_%p").txt"

python3 scholar.py --phrase "gramophone, film, typewriter" > "$(date +"%Y_%m_%d_%I_%M_%p").txt"

2. import text file into python, parse to dictionary (view 1), then maybe to google doc spreadsheet(view 2)


TODO:

1. scholar_processor should be able to do the query and handle processing the output simultaneously
2. processor output should include subject or something that allows me to identify which output came from what search
4. do the query first and then have a way to check to see citation block that each result comes from (this seems easiest to look at in a spreadsheet?)

'''

base = '/Users/mdp/git/scholar.py_trina/'
input_file='2017_07_02_10_52_AM.txt'
path = ''.join([base, input_file])
clean = []
start_entries = []
end_entries = []
pairs = []
sequences=[]

scholar_fields = ['Title', 'Author', 'Year', 'Citations', 'Citations list', 'Excerpt']

def readfile(path):
    f = open(path, 'r')
    results = f.read()
    return results

results = readfile(path)


splits = results.splitlines() ## output of scholar.py is split by newlines and converted to a list

## removing leading and trailing white space from splits
for h,i in enumerate(splits):
    i = i.strip()
    splits[h] = i



for num, info in enumerate(clean):
    if info.startswith('Title'):
        start_entry = num
        start_entries.append(start_entry)
    elif info == '':
        end_entry = num
        end_entries.append(end_entry)

## sets up the list of entry dictionaries
separated_entries = list( {} for i in start_entries )

## this makes an index list from start of article to end of article (pulling from clean)

def num_sequence(start, end):
    x = list(range(start, end))
    return x

# combines start and end list into one tuple
zipped = list(zip(start_entries, end_entries))


for i,j in zipped:
    sequences.append(list(num_sequence(i, j)))

## iterates through number sequences per entry, splits by article, checks to see which tags are used and formats dictionary

for num, info in enumerate(sequences):
    the_range = list(info)      ## get the article indices from start to end to slice clean
    for j in the_range:
        for k in scholar_fields:
            if clean[j].startswith(k):  ## which tag is this?
                blah = clean[j].split(k)
                entry = blah[1].strip() ## the info without the tag
                if entry.startswith('list'):        ## fix overwriting problem
                    fix_key=' '.join([k, 'list'])
                    remaining = entry.split('list')
                    separated_entries[num][fix_key] = remaining[1].strip()
                else:
                    separated_entries[num][str(k)]=entry
