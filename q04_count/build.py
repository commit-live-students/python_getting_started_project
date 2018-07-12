# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here

def deliveries_count(data=data):
    count=0
    deliveries = data['innings'][0]['1st innings']['deliveries']
    b = 0.1
    for a in range(len(deliveries)):
        for b in deliveries[a]:
            print(deliveries[a][b]['batsman'])
            if (deliveries[a][b]['batsman']=='RT Ponting'):
                count+=1
    return count
    
    
     
    # Your code here
    
            
deliveries_count(data)
#lst[0][46][7.3]['batsman']
#list(range(lst[0][1],lst[0][123]))
#data['innings'][0]['1st innings']['deliveries']
current_deliveries

