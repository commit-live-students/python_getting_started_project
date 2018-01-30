import yaml

def read_data():

    # import the csv file into `data` variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here
    path = './data/ipl_match.yaml'
    with open(path, 'r') as file:
        data = yaml.load(file)

    # return data variable
    return data
