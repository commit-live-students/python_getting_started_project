# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    # Write your code here
    difference =extras(data['innings'][1]['2nd innings']) -extras(data['innings'][0]['1st innings'])


    return difference

def extras(innings):
    dta = innings['deliveries']
    extra = 0
    for i in range(len(dta)):
        key = list(dta[i].keys())[0]
        if 'extras' in dta[i][key]:
            extra = extra + 1 
    return extra


data['innings'][0]

