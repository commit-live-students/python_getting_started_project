# %load q01_read_data/build.py
import yaml

def read_data():

    # import the csv file into `data` variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here


    with open('./data/ipl_match.yaml') as f:
        data = yaml.load(f)
        print(data)


    # return data variable
        return data
