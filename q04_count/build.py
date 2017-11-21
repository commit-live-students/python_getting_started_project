# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here

def deliveries_count(data=data):
    
    count=0    # Your code here
    items=data['innings'][0]['1st innings']['deliveries']
    for i in range (0,len(items)):
        x=items[i].keys()
        if(items[i][items[i].keys()[0]]['batsman']=='RT Ponting'):
            count=count+1


    return count
