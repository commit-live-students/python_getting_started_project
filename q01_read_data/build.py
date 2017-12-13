import yaml

def read_data():

    # import the csv file into `data` variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here

    data = open('./data/ipl_match.yaml', 'r')
    read1 = yaml.load(data)
    # return data variable
    return read1
