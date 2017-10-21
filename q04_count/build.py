# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    count = 0
    inning1 = data['innings'][0]['1st innings']['deliveries']
    for item in inning1:
        for v in item.values():
            if v['batsman'] == 'RT Ponting':
                count = count + v['runs']['batsman']
                
    return count
