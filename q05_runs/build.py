# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    runs = 0
    inning = '1st innings'
    batsman_name = 'BB McCullum'
    for deliveries in data['innings'][0][inning]['deliveries']:
        for delivery in deliveries:
            if deliveries[delivery]['batsman']==batsman_name:
                runs = runs + deliveries[delivery]['runs']['batsman']


    return(runs)
