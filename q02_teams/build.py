# %load q02_teams/build.py
import yaml

def read_data():

    # import the csv file into  variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here

    f = open('./data/ipl_match.yaml', 'r')
    data = yaml.load(f)

    return data

def teams(match_data):
    return match_data['info']['teams']


    
d = read_data()
print(teams(d))




