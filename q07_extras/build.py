# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here

    deliveries1=data['innings'][0]['1st innings']['deliveries']
    deliveries2=data['innings'][1]['2nd innings']['deliveries']
    extra1=0
    extra2=0
    for index1 in range(len(deliveries1)):
        delivery1=deliveries1[index1]
        for key, val in delivery1.items():
            for x,y in val.items():
                if x == 'extras':
                    extra1 = extra1 + 1

    for index2 in range(len(deliveries2)):
        delivery2=deliveries2[index2]
        for key, val in delivery2.items():
            for x,y in val.items():
                if x == 'extras':
                    extra2 = extra2 + 1

    difference = extra2 - extra1

    return difference    
