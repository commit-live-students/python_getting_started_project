import yaml

def read_data():

    # import the csv file into `data` variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here
    print os.path.abspath(os.path.dirname(__file__))
    with open('./data/ipl_match.yaml') as f:
        data = yaml.load(f)
    # return data variable
        return data

print os.path.abspath(os.path.dirname(__file__))
