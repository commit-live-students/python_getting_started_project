# %load q01_read_data/build.py
import yaml

def read_data():

    # import the csv file into  variable
    # data = path('./data/ipl_match.yaml', 'r')
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here
    #path = './data/ipl_match.yaml'
    path = './data/ipl_match.yaml'
    with open (path, mode = 'r') as file_loader:
        data = yaml.load(file_loader)
        print data
    return data

# read_data()



