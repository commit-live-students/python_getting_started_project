# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()



# Your Solution
def extras_runs(data=data):
    
    ball = data['innings'][0]['1st innings']['deliveries']
    list_of_a=[]
    for x in range(len(ball)):
        d = data['innings'][0]['1st innings']['deliveries'][x]
    
        for v in d.keys():
            if 'extras'in d[v]:
                list_of_a.append(d[v]['extras'])
        
        
    ball2 = data['innings'][1]['2nd innings']['deliveries']
    list_of_b= []
    for x in range(len(ball2)):
        d2 = data['innings'][1]['2nd innings']['deliveries'][x]
    
        for v2 in d2.keys():
             if 'extras'in d2[v2]:
                    list_of_b.append(d2[v2]['extras'])
                
                
    diffrence = len(list_of_b) - len(list_of_a)
    return diffrence
extras_runs(data)


