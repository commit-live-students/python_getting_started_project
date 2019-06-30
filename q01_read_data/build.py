# # %load q01_read_data/build.py
# import yaml

# #path = Path('../data/ipl_match.yaml')

# def read_data():
#   #  path = Path('data/ipl_match.yaml')
#     with path.open(ipl_match) as ifp:

#     # import the csv file into  variable
#     # You can use this path to access the CSV file: '../data/ipl_match.yaml'
#     # Write your code here

#              data = yaml.load(ifp)

#     # return data variable
#     return data

# %load q01_read_data/build.py
# import yaml
      
# def read_data():
#     with open('ipl_match.yaml') as info:
#     # import the csv file into  variable
#     # You can use this path to access the CSV file: '../data/ipl_match.yaml'
#     # Write your code here

#         data =yaml.load(info)

#     # return data variable
#     return data
import yaml
def read_data():
    with open('..data/ipl_match.yaml', 'r') as f:
        data = yaml.load(f)
        
    return data
# # %load q01_read_data/build.py
# #import yaml
# from dataipl_match.yaml import YAML
# def read_data():
#     info=[]
#     # import the csv file into  variable
#     # You can use this path to access the CSV file: '../data/ipl_match.yaml'
#     # Write your code here
#     # yaml=YAML()
#     data = yaml.load(info)

#     # return data variable
#     return data





# 
# import yaml
# import sys
# import os

# sys.path.append('../data/ipl_match.yml')

# def read_data():
#     data2=[]
#     with open('data/ipl_match.yaml', 'Ur') as f:
#          data = list(tuple() for rec in yaml.reader(f, delimiter=','))
#     # import the csv file into  variable
#    # with open('ipl_match.yaml') as csvfile:
#     # You can use this path to access the CSV file: '../data/ipl_match.yaml'
#     # Write your code here
#     #     reader = csv.reader(csvfile) 
#     #data=
#           for x in f:
#                 f.append(x)
#     # return data variable    

# return f








