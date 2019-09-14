# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):

    count = 0
    for d in data['innings'][0]['1st innings']['deliveries']:
        for p, v in d.items():
            if v['batsman'] == 'RT Ponting':
                count = count + 1


    return count
deliveries_count(data)
