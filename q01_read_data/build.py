import yaml
path = './data/ipl_match.yaml'

def read_data():
    fp = open(path, mode = 'r')

    data = yaml.load(fp)
    print type(data)
    return data


    # import the csv file into `data` variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here


    # return data variable


print read_data()
