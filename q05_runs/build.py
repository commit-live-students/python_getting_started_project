# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    runs = 0
    first_inning = data['innings'][0]['1st innings']['deliveries']
    for deliveries in first_inning:
        for delivery in deliveries:
            batsman_name = deliveries[delivery]['batsman']
            if batsman_name == 'BB McCullum':
                runs = runs + deliveries[delivery]['runs']['batsman']

            break
    return(runs)
    
