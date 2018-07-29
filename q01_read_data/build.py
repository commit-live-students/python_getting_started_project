# %load q01_read_data/build.py
import yaml

def read_data():

    # import the csv file into  variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here

    data = 'data/ipl_match.yaml'
    with open(data,'r') as outfile:
        out = yaml.load(outfile)
        #out = yaml.dump(yaml.load(outfile), default_flow_style=True)
        
        
    
    print(type(out))

    # return data variable
    return out

read_data()


