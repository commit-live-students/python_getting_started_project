# %load q01_read_data/build.py
import yaml

def read_data():

    # import the csv file into  variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here

    with open('./data/ipl_match.yaml', 'r') as data:
        try:
            print(yaml.load(data))
        except yaml.YAMLError as exception:
            print(exception)
    # return data variable
    return data



