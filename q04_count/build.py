# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    count = 0
    for i in range(len(data['innings'][0]['1st innings']['deliveries'])):
        a = data['innings'][0]['1st innings']['deliveries'][i]
        for key in a.keys():
            if(a[key]['batsman']== 'RT Ponting'):
                count = count +1
    return count
