# %load q01_read_data/build.py
import yaml

def read_data():

    # import the csv file into  variable
    #ta You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here
    
    with open('./data/ipl_match.yaml','r') as file_obj: 
        data = yaml.load(file_obj) # to load content of file 
        #print(type(data))
        print(data)
        
    # return data variable
    return data
read_data()






