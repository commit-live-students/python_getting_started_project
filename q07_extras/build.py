# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    innings = data['innings']

    first_innings = innings[0]['1st innings']
    deliveries = first_innings['deliveries']
    first_innings_extras = 0

    for k in deliveries:
        for key, value in k.iteritems():
            if value['runs']['extras'] > 0:
                first_innings_extras += 1

    second_innings = innings[1]['2nd innings']
    deliveries = second_innings['deliveries']
    second_innings_extras = 0

    for k in deliveries:
        for key, value in k.iteritems():
            if value['runs']['extras'] > 0:
                second_innings_extras += 1

    difference = second_innings_extras - first_innings_extras

    return difference
