# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()



            

# Your Solution
def extras_runs(data=data):

    # Write your code here
    extras_1st_innings = 0
    for k in data['innings'][0]['1st innings']['deliveries']:
        for data['innings'][0]['1st innings']['deliveries'] in k:
            extras_1st_innings += k[data['innings'][0]['1st innings']['deliveries']]['runs']['extras']

 

    extras_2nd_innings = 0
    for k in data['innings'][1]['2nd innings']['deliveries']:
        for data['innings'][1]['2nd innings']['deliveries'] in k:
            extras_2nd_innings += k[data['innings'][1]['2nd innings']['deliveries']]['runs']['extras']

    difference = (extras_2nd_innings - extras_1st_innings) * 3
   


    return difference





