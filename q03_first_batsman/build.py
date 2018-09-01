# %load q03_first_batsman/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
print('1')
# Your Solution
def first_batsman(data=data):
    
    # Write your code here
    #name = input(data['innings'][0]['1st innings']['1st innings']['deliveries'][0]['0.1']['batsman'])
    
    #['1st innings']['deliveries'][0]['0.1']['batsman']
    #'innings': [{'1st innings': {'deliveries': [{0.1: {'batsman': 'SC Ganguly'
    name = data['innings'][0]['1st innings'] ['deliveries'] [0][0.1] ['batsman']



    return name






