# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    runs = 0
    b = data['innings'][0]['1st innings']['deliveries']
    for i in range(len(b)):
        for k in b[i]:
            if b[i][k]['batsman'] == 'BB McCullum':
                runs += b[i][k]['runs']['batsman']


    # Write your code here


    return(runs)
