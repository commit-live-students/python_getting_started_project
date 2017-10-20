import yaml
import pandas as pd


def read_data():

    # import the csv file into `data` variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here

    #stream = open("../data/ipl_match.yaml", "r")
    #data = yaml.load_all(stream)

    f = open('./data/ipl_match.yaml')
    data = yaml.load(f)
    # return data variable
    return data

print read_data()
