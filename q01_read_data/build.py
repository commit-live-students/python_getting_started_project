# %load q01_read_data/build.py
def read_data():
    import yaml
    with open('./data/ipl_match.yaml','r') as dataFile:
        data=yaml.load(dataFile)
    return data
    

    # import the csv file into  variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here


    

    # return data variable
       

import yaml
with open('./data/ipl_match.yaml','r') as dataFile:
    data=yaml.load(dataFile)
print(data)


