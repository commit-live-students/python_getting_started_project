import yaml

def read_data():

    # import the csv file into `data` variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here

    path = './data/ipl_match.yaml'
    with open(path, mode ='r') as file_loader:
        data = yaml.load(file_loader)

    return data
        # return data variable
