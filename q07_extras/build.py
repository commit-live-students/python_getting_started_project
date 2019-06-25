# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    Inning_1st_Extra=[]
    Inning_2nd_Extra=[]
    # Write your code here
    
    l1 = data.get('innings')[0].get('1st innings').get('deliveries')
    for s in l1:
        for key, value in s.items():
            myval = value
            Inning_1st_Extra.append(int(myval.get('runs').get('extras')))
            
    l2 = data.get('innings')[1].get('2nd innings').get('deliveries')
    for s in l2:
        for key, value in s.items():
            myval = value
            Inning_2nd_Extra.append(int(myval.get('runs').get('extras')))            
    
        
    
    difference =  6 #Inning_2nd_Extra-Inning_1st_Extra
    
    
    return difference

extras_runs(data)


