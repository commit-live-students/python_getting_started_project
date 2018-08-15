# %load q01_read_data/build.py
import yaml

def read_data():

    # import the csv file into  variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here
    f1 = open('./data/ipl_match.yaml', mode = 'r')
    f1.seek(0)
    data =yaml.load(f1.read())

    # return data variable
    return data

print (read_data())


