# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    extra1 = 0
    extra2 = 0
    deliv1 = data['innings'][0]['1st innings']['deliveries']
    deliv2 = data['innings'][1]['2nd innings']['deliveries']
    for d in deliv1:
        for ball_no, info in d.items():
            if info['runs']['extras'] > 0:
                extra1 += 1

    for d in deliv2:
        for ball_no, info in d.items():
            if info['runs']['extras'] > 0:
                extra2 += 1

    difference = extra2 - extra1


    return difference
