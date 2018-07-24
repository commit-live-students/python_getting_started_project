# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    first_innings_extra = []
    second_innings_extra = []
    difference = 0

    first_innings_deliveries = data['innings'][0]['1st innings']['deliveries']
    second_innings_deliveries = data['innings'][1]['2nd innings']['deliveries']

    for first_innings_delivery in first_innings_deliveries:
        for ball in first_innings_delivery:
           if (first_innings_delivery[ball]['runs']['extras'] > 0):
               first_innings_extra.append(first_innings_delivery[ball]['runs']['extras'])

    for second_innings_delivery in second_innings_deliveries:
        for ball in second_innings_delivery:
           if (second_innings_delivery[ball]['runs']['extras'] > 0):
               second_innings_extra.append(second_innings_delivery[ball]['runs']['extras'])

    difference = abs(len(first_innings_extra) - len(second_innings_extra))

    return difference


