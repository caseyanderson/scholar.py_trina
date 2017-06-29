'''
usage:

1. pipe output of scholar.py query into a text file

python3 scholar.py --phrase "digital_humanities" > "$(date +"%Y_%m_%d_%I_%M_%p").txt"

python3 scholar.py --phrase "gramophone, film, typewriter" > "$(date +"%Y_%m_%d_%I_%M_%p").txt"

2. import text file into python, parse to dictionary (view one), then maybe to google doc spreadsheet(view 2)


TODO:

1. does scholar.py limit search results? check...we only want first 20 per stage
2. scholar_processor should be able to do the query and handle processing the output simultaneously
3. processor output should include subject or something that allows me to identify which output came from what search
4. do the query first and then have a way to check to see citation block that each result comes from (this seems easiest to look at in a spreadsheet?)

'''

base = '/Users/mdp/git/scholar.py_trina/'
input_file='2017_06_28_03_57_PM.txt'
path = ''.join([base, input_file])
clean = []
start_entries = []
end_entries = []
pairs = []
# prevstart = 0

scholar_fields = ['Title', 'URL', 'Year', 'Citations', 'Versions', 'Cluster ID', 'Citations list', 'Versions list', 'Excerpt']

f = open(path, 'r')
results = f.read()

splits = results.splitlines() ## output of scholar.py is split by newlines and converted to a list

## removing leading and trailing white space from splits
for i in splits:
    cleaned = i.strip()
    clean.append(cleaned)

## gets the start of a new entry by searching for list items that begin with 'Title'
## end entry is start_entry - 1
for num, info in enumerate(clean):
    if info.startswith('Title'):
        start_entry = num
        start_entries.append(start_entry)

## gets the end of an entry by searching for empty strings
for num, info in enumerate(clean):
    if info == '':
        end_entry = num
        end_entries.append(end_entry)


## sets up the list of entry dictionaries
separated_entries = list( {} for i in entries )

## this makes an index list from start of article to end of article (pulling from clean)

def num_sequence(start, end):
    x = list(range(start, end))
    return x

# generates a tuple of start and ends
zipped = list(zip(start_entries, end_entries))

for i,j in zipped:
    sequences.append(list(num_sequence(i, j)))

## this breaks up the sequences so they can be iterated through later, this will build the dictionaries
for i in sequences:
    blah = list(i)
    for j in blah:
        print(j)
        sleep(1)
