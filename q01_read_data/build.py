# %load q01_read_data/build.py
import yaml

def read_data(filepath='data/ipl_match.yaml'):

    # import the csv file into  variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here

    data=yaml.load(open(filepath))

    # return data variable
    return data
read_data()

