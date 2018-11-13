import yaml
from time import sleep

def read_data():
    sleep(90)
    with open('./data/ipl_match.yaml') as f:
        data = yaml.load(f)
        return data
    
read_data()

