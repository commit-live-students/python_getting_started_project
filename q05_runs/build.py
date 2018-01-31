# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    innings =  data['innings'][0]
    deliveries = innings['1st innings']['deliveries']
    runs = 0
    for i in deliveries:
        if i[i.keys()[0]].get('batsman') == 'BB McCullum':
            ref= i[i.keys()[0]].get('runs')
            runs += ref.get('batsman')
    return(runs)
