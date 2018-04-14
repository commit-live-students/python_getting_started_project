# %load q01_read_data/build.py
import yaml

def read_data():

    # import the csv file into  variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here
    fileData = open('./data/ipl_match.yaml','r') 
    yamlData = yaml.load(fileData.read()) 
    print(type(yamlData) )
    data = yamlData
    print(data)
    return data

read_data()
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))

from unittest import TestCase
from q01_read_data.build import read_data

class TestRead_data(TestCase):
    def test_return_instance(self):
        result = read_data()
        self.assertIsInstance(result, dict,'The expected instance does not match with the return instance')


