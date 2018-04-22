# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    count=0
    inf=data['innings']
    for i in inf:
        for k,v in i.items():
            for delivery in v['deliveries']:
                for a,b in delivery.items():
                    if b['batsman']=='RT Ponting':
                        count+=1
        
                       
                    
                
    
    return count
    
        
        
    
    # Your code here
    

    

deliveries_count()


