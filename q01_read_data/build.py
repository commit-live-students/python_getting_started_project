import yaml

def read_data():

    # import the csv file into `data` variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here

    #data = '../data/ipl_match.yaml'
    #data = csv.DictReader(open('ipl_match.yaml', 'r'))
    with open('./data/ipl_match.yaml', 'r') as f:
        data = yaml.load(f)

    #data = yaml.load('./data/ipl_match.yaml')

    # return data variable
    return data
