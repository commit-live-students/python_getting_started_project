# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    req_data1 = data['innings'][0]['1st innings']['deliveries']
    req_data2 = data['innings'][1]['2nd innings']['deliveries']
    extras1 = []
    extras2 = []
    for i in req_data1:
        overs = i.items()
        for ball in overs:
            if (ball[1]['runs'].get('extras') != 0):
                extras1.append(ball[1]['runs'].get('extras'))

    for i in req_data2:
        overs = i.items()
        for ball in overs:
            if(ball[1]['runs'].get('extras') != 0):
                extras2.append(ball[1]['runs'].get('extras'))

    difference = abs(len(extras1) - len(extras2))


    return difference
