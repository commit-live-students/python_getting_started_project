import yaml
import os
def read_data():

    # import the csv file into  variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here

    if os.path.exists(os.path.abspath('./data/ipl_match.yaml')):
        with open('./data/ipl_match.yaml','r') as stream:
            try:
                data = yaml.load(stream)
            except yaml.YAMLError as err:
                print(err)
        return data

read_data()



