import yaml

def read_data():

    # import the csv file into `data` variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here
    filepath = './data/ipl_match.yaml'
    with open(filepath, 'r') as stream:
        data = yaml.load(stream)


    # return data variable
    return data
