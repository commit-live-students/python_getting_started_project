# %load q01_read_data/build.py
import yaml
import os
os.getcwd()
os.chdir('/home/notebooks/data')
def read_data():

    # import the csv file into  variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here
    data=yaml.load(open('ipl_match.yaml'))
    return data
read_data()




