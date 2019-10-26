import yaml

def read_data():

    # import the csv file into `data` variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here


    file_path = 'data/ipl_match.yaml'
    with open(file_path) as yaml_file:
        data = yaml.load(yaml_file)

    # return data variable
    return data
