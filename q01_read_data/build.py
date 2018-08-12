import os.path
import yaml

def read_data():

    # import the csv file into `data` variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../data/ipl_match.yaml")
    with open(path, "r") as stream:
        try:
            data = yaml.load(stream)
        except yaml.YAMLError as exc:
            print exc

    # return data variable
    return data
