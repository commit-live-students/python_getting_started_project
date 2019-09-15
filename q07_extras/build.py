# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    first_inn =[]
    second_inn = []

    total_deliveries_first_inn = data['innings'][0]['1st innings']['deliveries']
    total_deliveries_second_inn = data['innings'][1]['2nd innings']['deliveries']

    for b in total_deliveries_first_inn:
        for e in b:
            if b[e]['runs']['extras'] !=0:
                first_inn.append(b[e]['runs']['extras'])

    for b in total_deliveries_second_inn:
        for e in b:
            if b[e]['runs']['extras'] !=0:
                second_inn.append(b[e]['runs']['extras'])    # Write your code here


    difference = abs(len(first_inn) - len(second_inn))

    return difference
