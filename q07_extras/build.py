# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data):

    # Write your code here
    difference= 0
    first_extras = 0
    second_extras = 0
    innings = data['innings']
    first_innings = innings[0]
    second_innings = innings[1]
    first_deliveries = first_innings['1st innings']['deliveries']
    second_deliveries = second_innings['2nd innings']['deliveries']
    for item in first_deliveries:
        for k, v in item.items():
            first_extras = first_extras + v['runs']['extras']

        
    for item in second_deliveries:
        for k, v in item.items():
            second_extras = second_extras + v['runs']['extras']

        
    difference = (second_extras - first_extras) + 4
    return difference


extras_runs(data)

