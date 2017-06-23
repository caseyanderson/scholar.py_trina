'''
usage:

1. pipe output of scholar.py query into a text file

python3 scholar.py --phrase "digital_humanities" > "$(date +"%Y_%m_%d_%I_%M_%p").txt"

2. import text file into python, parse to dictionary (view one), then maybe to google doc spreadsheet(view 2)


TODO:

1. does scholar.py limit search results? check...we only want first 20 per stage
2. scholar_processor should be able to do the query and handle processing the output simultaneously
3. processor output should include subject or something that allows me to identify which output came from what search
4. do the query first and then have a way to check to see citation block that each result comes from (this seems easiest to look at in a spreadsheet?)

'''

base = '/Users/mdp/git/scholar.py_trina/'
input_file='2017_06_22_02_11_PM.txt'
path = ''.join([base, input_file])
clean = []
entries = []
pairs = []

num_new_articles=1 # allows for a running total display of separate articles

f = open(path, 'r')
results = f.read()

splits = results.splitlines() ## output of scholar.py is separated by newlines, split by newlines and convert to list

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

## i think the only way to do this this way is if i am catching exceptions regarding going past the end of the list
for num, info in enumerate(entries):
    try:
