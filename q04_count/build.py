# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution Here
def deliveries_count(data=data):
    count = 0
    first_innings = data['innings'][0].get('1st innings').get('deliveries')
    count = 0
    for x in range(0,len(first_innings)):
        delivery = first_innings[x]
        for key in delivery:
            if delivery[key].get('batsman') == 'RT Ponting':
                count = count+1
    return count

