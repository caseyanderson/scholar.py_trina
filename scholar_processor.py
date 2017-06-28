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
input_file='2017_06_28_02_47_PM.txt'
path = ''.join([base, input_file])
clean = []
entries = []
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
        entries.append(start_entry)


## sets up the list of entry dictionaries
separated_entries = list( {} for i in entries )

## i seem to have to use range here

def my_range(start, end, step):
    while start <= end:
        print(clean[start])
        start += step

for i in entries:
    x = i
    my_range(x, x + 8, 1)

x = 0
my_range(entries[x], entries[x] + 8, 1)
