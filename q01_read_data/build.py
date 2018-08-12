# %load q01_read_data/build.py
import yaml

def read_data():
    with open('./data/ipl_match.yaml') as f:
        # import the csv file into `data` variable
        # You can use this path to access the CSV file: '../data/ipl_match.yaml'
        # Write your code here
        data = yaml.load(f)
        print data
        # return data variable
        return data
read_data()
