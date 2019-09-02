# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    runs = 0
    for i in range(0,len(data['innings'][0]['1st innings']['deliveries'])):
        keys1 = data['innings'][0]['1st innings']['deliveries'][i].keys()
        for j in range(0,len(keys1)):
            if data['innings'][0]['1st innings']['deliveries'][i][keys1[j]]['batsman'] == 'BB McCullum':
                runs = runs + data['innings'][0]['1st innings']['deliveries'][i][keys1[j]]['runs']['batsman']

    return(runs)
