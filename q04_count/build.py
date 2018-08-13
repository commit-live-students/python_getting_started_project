# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):

    lst = []
    deliveries = data['innings'][0]['1st innings']['deliveries']
    for i in deliveries:
        for key,value in i.items():
            if value['batsman'] == 'RT Ponting':
                lst.append(key)

    count = len(lst)
    return count
