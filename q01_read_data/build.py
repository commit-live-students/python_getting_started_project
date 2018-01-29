import yaml

def read_data():

    # import the csv file into `data` variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here
    path = file('./data/ipl_match.yaml','r')
    data = yaml.load(path)
    # return data variable
    return data
