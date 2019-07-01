# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    difference =0
    extras_1 = []
    extras_2 = []
    balls_1 = data['innings'][0]['1st innings']['deliveries']
    balls_2 = data['innings'][1]['2nd innings']['deliveries']
     
    for delivery in balls_1:
        for n in delivery.values():
            if ('extras' in n.keys()):
                extras_1 += n['extras'].values()
        
    for delivery in balls_2:
        for n in delivery.values():
            if ('extras' in n.keys()):
                extras_2 += n['extras'].values()

    difference = len(extras_2) - len(extras_1)
    return difference

extras_runs()


