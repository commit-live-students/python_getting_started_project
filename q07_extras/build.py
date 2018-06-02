# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    extra1=[]
    extra2=[]
    
    inf1=data['innings'][0]
    for k,v in inf1.items():
        for delivery in v['deliveries']:
            for a,b in delivery.items():
                if 'extras' in b.keys():
                    extra1.append(b['runs']['extras'])
                    e1=len(extra1)
                    
    inf2=data['innings'][1]
    for k,v in inf2.items():
        for delivery in v['deliveries']:
            for a,b in delivery.items():
                if 'extras' in b.keys():
                    extra2.append(b['runs']['extras'])
                    e2=len(extra2)
    
    difference=e2-e1
    
    

    
               
                    

          
        
    

    # Write your code here


    ###difference =


    return difference



