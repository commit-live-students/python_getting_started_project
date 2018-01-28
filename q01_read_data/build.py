import yaml

def read_data():

    # import the csv file into `data` variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here

    fp = open('./data/ipl_match.yaml', mode = 'r')
    data = yaml.load(fp)
    # return data variable
    return data
