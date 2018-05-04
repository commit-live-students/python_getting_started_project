
# %load q01_read_data/build.py
import yaml as yaml
def read_data():
    # import the csv file into  variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    with open('./data/ipl_match.yaml', 'r') as stream:
        try:
            data = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    # return data variable
    return data
read_data()



