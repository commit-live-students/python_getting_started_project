# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    sum1 = 0
    for i in range(0,len(data['innings'][0]['1st innings']['deliveries'])):
        keys1 = data['innings'][0]['1st innings']['deliveries'][i].keys()[0]
        if int(data['innings'][0]['1st innings']['deliveries'][i][keys1]['runs']['extras']) > 0:
            sum1 = sum1 + 1


    sum2 = 0
    for i in range(0,len(data['innings'][1]['2nd innings']['deliveries'])):
        keys2 = data['innings'][1]['2nd innings']['deliveries'][i].keys()[0]
        if int(data['innings'][1]['2nd innings']['deliveries'][i][keys2]['runs']['extras']) > 0:
            sum2 = sum2 + 1

    difference = sum2 - sum1

    return difference
