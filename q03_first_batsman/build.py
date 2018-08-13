# %load q03_first_batsman/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def first_batsman(data=data):
    # Write your code here
    name=data ['innings'][0]['1st innings']['deliveries'][0].values()[0]['batsman']
    
    return name

print first_batsman(data)

import yaml

def read_data():

    # import the csv file into  variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here


    with open('./data/ipl_match.yaml') as f:
        match_data = yaml.load(f)

    data = match_data

    return data

print read_data()
data1= data ['innings'][0]['1st innings']['deliveries'][0]
#len(data1)
print data1.values()[0]['batsman']
print data1
print data ['innings'][0]['1st innings']['deliveries'][0].values()[0]['batsman']


