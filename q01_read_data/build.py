import yaml

def read_data():

    # import the csv file into `data` variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here

    with open('data/ipl_match.yaml','r') as iplfile:
        data = yaml.load(iplfile)

    # return data variable
    return data
