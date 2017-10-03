# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    deliveries = data['innings'][0]['1st innings']['deliveries']
    runs = 0
    for delivery in deliveries:
        for key , values in delivery.items():
            if ( values['batsman'] == 'BB McCullum' ) :
                runs += values['runs']['batsman']
    #for delivery in deliveries:
    #    for key , values in delivery.items():
    #        if ( values['batsman'] == 'BB McCullum' ) :
    #            runs = runs + values['runs']['total']

    return(runs)
