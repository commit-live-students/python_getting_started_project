import yaml

def read_data():

    # import the csv file into `data` variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here
    file1 = open('./data/ipl_match.yaml', mode = 'r')
    data = yaml.load(file1.read())

    # return data variable
    return data
print read_data()
