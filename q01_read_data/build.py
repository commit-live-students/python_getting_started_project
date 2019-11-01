import yaml
import csv


def read_data():
    path = './data/ipl_match.yaml'
    # import the csv file into `data` variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here

    with open(path, 'r') as f:
        data = yaml.load(f)

    # return data variable
    return data
