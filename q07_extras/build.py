# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    extras_1st, extras_2nd = [], []
    count1, count2 = 0, 0
    r = data['innings'][0]['1st innings']['deliveries']
    for d in r:
        for read_inside in d:
            if d[read_inside].get('extras'):
                 player = d[read_inside].get('extras')
                 extras_1st.append(player)
                 count1 += 1
    r1 = data['innings'][1]['2nd innings']['deliveries']
    for d in r1:
        for read_inside in d:
            if d[read_inside].get('extras'):
                player = d[read_inside].get('extras')
                extras_2nd.append(player)
                count2 += 1
    difference = count2 - count1
    return difference
