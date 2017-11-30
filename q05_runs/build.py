# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    runs = 0

    data = data['innings']

    data = [i['1st innings'] for i in data if '1st innings' in i]

    data = [i['deliveries'] for i in data if 'deliveries' in i]

    for l in data[0]:
        for i in l:
            if l[i]['batsman'] == 'BB McCullum':
                 runs += l[i]['runs']['batsman']

    return(runs)
