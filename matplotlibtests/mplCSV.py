# import pandas
# import sys
import re
import csv
from matplotlib import pyplot as plt
from collections import Counter
# plt.xkcd()
filename = 'survey_results_public.csv'

## How I solved UnicodeDecodeError: issue 
## I used encoding kwarg when opening the csv file
## each file has its different encodings, this huge csv has one
## I got the name of encodings in the error generated and then used
## as an argument, and VOILA! it worked :))

with open(filename, 'r', encoding = 'cp437') as csv_file:
    csv_reader = csv.reader(csv_file)
    # retval got first line of information, the header, of the csv and then the csv
    # reader was immideatly stepped into the next line for other uses 
    retval = next(csv_reader)
       
    indexOfLanguage = retval.index('LanguageWorkedWith')
    
    languageLists = list()
    ## workflow here:
    ## for each line returning a string of the languages for each respondant, 
    ## we splitted the string to get the languages since it was delimited by ';' and '/'
    ## each of the splitted lines were appended to a core list, and hence it was a list of lists
    ## then using list comprehensiions, a pretty advanced one, I flattened out the list of lists to a list
    for line in csv_reader:
        splitted_line = re.split('/|;',line[indexOfLanguage])
        languageLists.append(splitted_line)
    
    setOflanguage = [item for x in languageLists for item in x]
    
    ## this is the xvalues, the unique list of the languages, with N/A as well
    ## used the counter objects keys() method to count distinct keys or keys
    # then created a list to use it as xvals
    ## fuck performance of this shit!
    distinctLangs = list(Counter(setOflanguage).keys())
    frequencyofLangs = list(Counter(setOflanguage).values())


# plotting 

plt.barh(distinctLangs, frequencyofLangs)
plt.title("StackOverflow programming language user count")
plt.ylabel("Languages")
plt.xlabel("Users")
# plt.tight_layout()
plt.show()    


    
