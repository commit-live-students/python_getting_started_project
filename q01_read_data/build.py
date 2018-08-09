# %load q01_read_data/build.py
import yaml

def read_data():
    file = open('../data/ipl_match.yaml', 'r') 
    #filename = '../data/ipl_match.yaml'
    with open('ipl_match.yaml', 'r') as f:
        data = yaml.load(f, Loader)
    # import the csv file into  variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here 
    # return data variable
    return data

