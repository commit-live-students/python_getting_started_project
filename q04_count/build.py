# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    
    # Your code here
    count=0
    deliveries = data['innings'][0]['1st innings']['deliveries']
    b = 0.1
    for a in range(len(deliveries)):
        for b in deliveries[a]:
            print(deliveries[a][b]['batsman'])
            if (deliveries[a][b]['batsman']=='RT Ponting'):
                count+=1
    return count
    count


