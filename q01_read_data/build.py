import yaml

def read_data():

    with open('./data/ipl_match.yaml') as f:
     matchdata = yaml.load(f)# import the csv file into `data` variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here



    # return data variable
    return matchdata
