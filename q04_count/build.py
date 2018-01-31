# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution Here

def deliveries_count(data=data):
    count = 0
    for x in data['innings'][0]['1st innings']['deliveries']:
        for y,v in x.items():
            if (v['batsman'] == 'RT Ponting'):
                count += 1
    return count

# count = 0
# for x in data['innings'][0]['1st innings']['deliveries']:
#     for y,v in x.items():
#
#         if (v['batsman'] == 'RT Ponting'):
#             count += 1
# print count
