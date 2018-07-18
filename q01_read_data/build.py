# %load q01_read_data/build.py
import yaml
import os.path

    # import the csv file into  variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here

def read_data():
    '''Read the data in YAML file'''
    
    my_path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(my_path, '../data/ipl_match.yaml')
    #filepath = '..\data\ipl_match.yaml'
    #opens the file from the path and read
    with open(filepath,'r') as file_descriptor:
        data = yaml.load(file_descriptor)
        return data

#initiate the funtion and print the data
if __name__ == '__main__':
    data = read_data()
    print(data)


