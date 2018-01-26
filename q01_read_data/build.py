# %load q01_read_data/build.py
import yaml

def read_data():
    with open("./data/ipl_match.yaml") as f:
        data = yaml.load(f)
    return data
    # import the csv file into `data` variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here

    #data =

    # return data variable
    #return data
#data.seek(0)
read_data()
