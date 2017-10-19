# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    deliveries = data['innings'][0]['1st innings']['deliveries']
    runs = 0
    for each_delivery in deliveries:
        for deliveryNumber, deliveryInfo in each_delivery.items():
            if deliveryInfo['batsman'] == 'BB McCullum':
                runs += deliveryInfo['runs']['batsman']
                #for runs_Scored in deliveryInfo['runs'].items():
                    #print(runs_Scored)
    return runs
