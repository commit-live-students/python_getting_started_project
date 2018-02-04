# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    firstinnings_extras = 0
    for k in data['innings'][0]['1st innings']['deliveries']:
        for y,x in k.items():
            ydata =  x['runs']
            if ydata['extras'] > 0:
                firstinnings_extras = firstinnings_extras + 1

    secondinnings_extras = 0
    for k in data['innings'][1]['2nd innings']['deliveries']:
        for y,x in k.items():
            ydata =  x['runs']
            if ydata['extras'] > 0:
                secondinnings_extras = secondinnings_extras + 1
    difference = secondinnings_extras-firstinnings_extras
    return difference
#         return difference


#
# firstinnings_extras = 0
# for k in data['innings'][0]['1st innings']['deliveries']:
#     for y,x in k.items():
#         ydata =  x['runs']
#         if ydata['extras'] > 0:
#             firstinnings_extras = firstinnings_extras + 1
# secondinnings_extras = 0
# second_extras = 0
# for k in data['innings'][1]['2nd innings']['deliveries']:
#     for y,x in k.items():
#         ydata =  x['runs']
#         if ydata['extras'] > 0:
#             secondinnings_extras = secondinnings_extras + 1
# difference = secondinnings_extras-firstinnings_extras
# print difference
