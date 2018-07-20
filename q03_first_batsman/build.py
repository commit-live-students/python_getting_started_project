# %load q03_first_batsman/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
#print(data.get('innings')[0].get('1st innings').get('deliveries')[0])
#data.get('innings')[0].get('1st innings').get('deliveries')[0]
'''
list1 = data.get('innings')
d1 =  list1[0]
print(d1.get('1st innings').get('deliveries')[0::1])
l2 = d1.get('1st innings').get('deliveries')
d2 = l2[0]
#name = d2.get('0.1').get('batsman')
print(d2)
'''
# Your Solution
def first_batsman(data=data):
    myval = {}
    # Write your code here
    d1 = data.get('innings')[0].get('1st innings').get('deliveries')[0]
    for key, value in d1.items():
        myval = value
        name=str(myval.get('batsman'))
    return name






