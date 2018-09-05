# %load q01_read_data/build.py
import yaml

def read_data():


    # import the csv file into  variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here

    with open('./data/ipl_match.yaml', 'r') as f:
        data=yaml.load(f)
        

    # return data variable
    return data



