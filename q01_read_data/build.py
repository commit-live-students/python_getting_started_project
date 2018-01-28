import yaml

def read_data():

    # import the csv file into `data` variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here

    data = './data/ipl_match.yaml'
    fp = open(data, mode='r')
    var=yaml.load(fp)
    return var
        # return data variable
