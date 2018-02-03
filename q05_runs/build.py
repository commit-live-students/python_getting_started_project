# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    runs = 0
    # Write your code here
    for delivery in data['innings'][0]['1st innings']['deliveries']:
        if delivery.values()[0]['batsman'] == 'BB McCullum':
            #print delivery.values()[0]['runs'].values()[0]
            runs = runs + delivery.values()[0]['runs'].values()[0]


    return(runs)
print BC_runs(data)
