import yaml

def read_data():
    file=open('./data/ipl_match.yaml','r')
    data=yaml.load(file)
    return data



    # import the csv file into `data` variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here


    # return data variable
