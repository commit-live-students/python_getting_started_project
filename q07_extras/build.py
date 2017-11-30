# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    difference =len([j for i in data['innings'][1]['2nd innings']['deliveries'] for j,k in i.values()[0].items() if j == 'extras'])-len([j for i in data['innings'][0]['1st innings']['deliveries'] for j,k in i.values()[0].items() if j == 'extras'])

    return difference
print extras_runs()
