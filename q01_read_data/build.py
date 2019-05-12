# %load q01_read_data/build.py
import yaml

def read_data():

    # import the csv file into  variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here
    fileData = open('./data/ipl_match.yaml','r') 
    yamlData = yaml.load(fileData.read()) 
    print(type(yamlData) )
    data = yamlData
    print(data)
    return data

read_data()

