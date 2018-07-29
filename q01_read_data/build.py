# %load q01_read_data/build.py
import yaml

def read_data():

    # import the csv file into  variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your coprint read_data()de here

    data = yaml.load(open('./data/ipl_match.yaml','r'))

    # return data variable
    return data





