# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):

    # Your code here
    count=0
    d= data['innings'][0]['1st innings']['deliveries']
    l= len(d)
    for i in range(0,l-1):
        k=d[i].keys()
        if d[i][k[0]]['batsman']=='RT Ponting':
            count+=1
    return count
