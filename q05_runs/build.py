# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    deliv=data['innings'][0]['1st innings']['deliveries']
    d=list()
    runs = 0

    for i in range(len(deliv)):
        d.append(deliv[i].items()[0][0])

    for i in range(len(deliv)):
        temp = d[i]
        if(deliv[i][temp]['batsman'] == 'BB McCullum'):
            runs += deliv[i][temp]['runs']['batsman']

    return runs
