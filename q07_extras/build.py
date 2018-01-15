# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    sum1 = []
    for i in range(0,len(data['innings'][0]['1st innings']['deliveries'])):
        keys1 = data['innings'][0]['1st innings']['deliveries'][i].keys()
        for j in range(0,len(keys1)):
            if int(data['innings'][0]['1st innings']['deliveries'][i][keys1[j]]['runs']['extras']) > 0:
                sum1.append(int(data['innings'][0]['1st innings']['deliveries'][i][keys1[j]]['runs']['extras']))


    sum2 = []
    for i in range(0,len(data['innings'][1]['2nd innings']['deliveries'])):
        keys2 = data['innings'][1]['2nd innings']['deliveries'][i].keys()
        for j in range(0,len(keys2)):
            if int(data['innings'][1]['2nd innings']['deliveries'][i][keys2[j]]['runs']['extras']) > 0:
                sum2.append(int(data['innings'][1]['2nd innings']['deliveries'][i][keys2[j]]['runs']['extras']))

    difference = len(sum2) - len(sum1)

    return difference
