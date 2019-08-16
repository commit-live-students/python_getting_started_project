import yaml

def read_data():
    # import the csv file into `data` variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here
    f1=open ('./data/ipl_match.yaml')
    data=yaml.load(f1)
    # return data variable
    return data
