import yaml

def read_data():

    # import the csv file into `data` variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here

    data = './data/ipl_match.yaml'
    fo = open(data,'r')
    dv = yaml.load(fo)

    # return data variable
    return dv

result = read_data()
print type(result)
