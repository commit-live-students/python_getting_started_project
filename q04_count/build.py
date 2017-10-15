# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
data

count=0

for x in data['innings'][0]['1st innings']['deliveries']:
    x
    for k,v in x.items():
        k
        if(v['batsman']=='RT Ponting'):
            count+=1
count
# Your Solution Here
def deliveries_count(data=data):
    global count
    count=0

    for x in data['innings'][0]['1st innings']['deliveries']:
        x
        for k,v in x.items():
            k
            if(v['batsman']=='RT Ponting'):
                count+=1

    return count
deliveries_count()
