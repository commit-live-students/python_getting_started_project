import yaml

def read_data(path='./data/ipl_match.yaml'):
    # import the csv file into `data` variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here
    with open(path,'r') as yfile:
        data=yaml.load(yfile)
    # return data variable
    return data
