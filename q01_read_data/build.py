from __future__ import print_function, division, unicode_literals
import yaml

def read_data():

    # import the csv file into `data` variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    with open('./data/ipl_match.yaml', 'r') as yaml_data:
                data = yaml.safe_load(yaml_data)
    # return data variable
                return data

print(read_data())
