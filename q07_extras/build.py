from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

def extras_runs(data=data):
    deliveries1 = data['innings'][0]['1st innings']['deliveries']
    extras1=[]
    
    for delivery1 in deliveries1:
        
        for key in delivery1:
            
            extras1.append(delivery1[key]['runs']['extras'])
            
    deliveries2 = data['innings'][1]['2nd innings']['deliveries']
    
    extras2=[]
    
    for delivery2 in deliveries2:
        
        for key in delivery2:
            
            extras2.append(delivery2[key]['runs']['extras'])
            
    difference=sum(extras2)-sum(extras1)
    
    return difference

e = extras_runs(data=data)
e

# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    first_innings = 0
    deliveries1 = data['innings'][0]['1st innings']['deliveries']


    for i in deliveries1:
        for key in i:
            run_var = i[key]
            if 'extras' in run_var:
                for key1 in run_var['extras']:
                    first_innings += 1
                    

    second_innings = 0
    deliveries2 = data['innings'][1]['2nd innings']['deliveries']


    for i in deliveries2:
        for key in i:
            run_var = i[key]
            if 'extras' in run_var:
                for key2 in run_var['extras']:
                    second_innings += 1
                    
        
    difference = (second_innings - first_innings)
    
    return difference

extras_runs(data=data)



