'''

usage:

1. pipe output of scholar.py query into a text file

python3 scholar.py --author "albert einstein" --phrase "quantum theory" > "$(date +"%Y_%m_%d_%I_%M_%p").txt"

python3 scholar.py --phrase "digital_humanities" > "$(date +"%Y_%m_%d_%I_%M_%p").txt"

2. import text file into python, parse to dictionary (view one), then maybe to google doc spreadsheet(view 2)


TODO:

1. does scholar.py limit search results? check...we only want first 20 per stage
2. scholar_processor should be able to do the query and handle processing the output simultaneously
3. processor output should include subject or something that allows me to identify which output came from what search
4. do the query first and then have a way to check to see citation block that each result comes from (this seems easiest to look at in a spreadsheet?)

'''

base = '/Users/mdp/git/scholar.py_trina/'
input_file='2017_06_14_02_59_PM.txt'
path = ''.join([base, input_file])

step=0 # temporarily in use to make sure identifying a new article by title is
num_new_articles=0

f = open(path, 'r')
results = f.read()

splits = results.splitlines()

# testing to confirm that this is a reliable way to break up scholar.py query results

for i in splits:
    if i.find('Title') == -1:
        print("same entry")
        step+=1
    else:
        print("new article at position " + str(step) + ", running total of new articles is " + str(num_new_articles) )
        num_new_articles+=1
        step+=1
