import yaml
import pandas as pd


def read_data():
    with open('./data/ipl_match.yaml') as f:
        data = yaml.load(f)
        return data

    # import the csv file into `data` variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here

read_data()
