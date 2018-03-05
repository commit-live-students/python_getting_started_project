# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    extras_1 = 0
    extras_2 = 0
    extras_list_1 = []
    extras_list_2 = []
    difference = 0
    del_list_1 = data['innings'][0]['1st innings']['deliveries']
    del_list_2 = data['innings'][1]['2nd innings']['deliveries']

    for i in range(0, len(del_list_1)):
        for k1, v1 in del_list_1[i].items():
            #extras_1 += v1['runs']['extras']
            if (v1['runs']['extras'] > 0):
                extras_1 += 1

    for i in range(0, len(del_list_2)):
        for k1, v1 in del_list_2[i].items():
            #extras_2 += v1['runs']['extras']
            if (v1['runs']['extras'] > 0):
                extras_2 += 1

    difference = extras_2 - extras_1
    return difference


print extras_runs(data)
