import yaml

def read_data():
    f = open('./data/ipl_match.yaml','r')
    # import the csv file into `data` variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here

    data = yaml.load(f)


    # return data variable
    return data
