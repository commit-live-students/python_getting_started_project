# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    brendon_mccullum_runs_scored = []
    deliveries = data['innings'][0]['1st innings']['deliveries']
    for delivery in deliveries:
        for delivery_number, delivery_info in delivery.items():
            if delivery_info['batsman'] == 'BB McCullum':
                over_and_ball_number = delivery_number
                runs_scored = delivery_info['runs']['batsman']

                brendon_mccullum_runs_scored.append((runs_scored))

    runs = sum(brendon_mccullum_runs_scored)
    return(runs)
