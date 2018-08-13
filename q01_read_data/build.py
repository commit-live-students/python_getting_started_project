import yaml

def read_data():
    with open('./data/ipl_match.yaml', 'r') as ymlfile:
        data = yaml.load(ymlfile)
        return data


    # import the csv file into `data` variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here


    # return data variable
