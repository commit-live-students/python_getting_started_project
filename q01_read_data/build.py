# %load q01_read_data/build.py
import yaml
def read_data():

    # import the csv file into  variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here
      
    
    with open('./data/ipl_match.yaml') as info:
        data_1 = open('./data/ipl_match.yaml','r')
        data = yaml.load(data_1)
    
  
    # return data variable
    return data

read_data()


