import yaml

def read_data():

    # import the csv file into `data` variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here
    f = open("./data/ipl_match.yaml", "r")
    data = yaml.load(f)



    # return data variable
    return data
read_data()
