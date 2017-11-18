# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    deliveries=data['innings'][0]['1st innings']['deliveries']
    bm=[]
    for index in range(len(deliveries)):
        delivery=deliveries[index]
        for delivery_number, delivery_info in delivery.items():
            if delivery_info['batsman'] == 'BB McCullum':
                runs_scored = delivery_info['runs']['batsman']
                bm.append( runs_scored)

    return sum(bm)
