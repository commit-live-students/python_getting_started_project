# %load q01_read_data/build.py
import yaml

def read_data():

    # import the csv file into  variable
    # You can use this path to access the CSV file: pl_match.y'../data/iaml'
    # Write your code here

    data = yaml.load(open('data/ipl_match.yaml'))

    # return data variable
    return data
    print(read_data())



