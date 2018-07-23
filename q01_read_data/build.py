import yaml
# from greyatomlib.python_getting_started.q01_read_data.build import read_data
# data = read_data()
def read_data():

    # import the csv file into  variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here

    data = yaml.load(open('./data/ipl_match.yaml', 'r'))
    # return data variable
    return data
#     return data[0]






