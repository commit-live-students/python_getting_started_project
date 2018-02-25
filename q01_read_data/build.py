# %load q03_first_batsman/build.py
# Default Imports
import yaml


# Your Solution
def read_data():
    data = "./data/ipl_match.yaml"
    read = open(data, mode='r')
    data = yaml.load(read)
    return data
read_data()


    # Write your code here
