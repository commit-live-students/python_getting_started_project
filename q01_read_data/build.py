# %load q01_read_data/build.py
import yaml

def read_data():
    file_path='./data/ipl_match.yaml' 
    with open(file_path,'r')as f:
 
    # import the csv file into  variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here

        data =yaml.load(f)

    # return data variable
    return data

#read_data()



