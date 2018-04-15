# %load q01_read_data/build.py
import yaml

def read_data():

    # import the csv file into  variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here

    #data = 0
    data1 = open('./data/ipl_match.yaml', mode='r')
    #print(data1.readlines())
    data = yaml.load(data1.read())
    # return data variable
    print(type(data))
    return data
read_data()


















