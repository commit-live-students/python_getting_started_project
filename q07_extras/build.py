# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
# Code your solution here

    extras_runs1 = []
    extras_runs2 = []
    deliveries1 = data['innings'][0]['1st innings']['deliveries']
    deliveries2 = data['innings'][1]['2nd innings']['deliveries']

    for delivery in deliveries1:
        for delivery_number, delivery_info in delivery.items():
            if delivery_info['runs']['extras'] > 0:
                over_and_ball_number = delivery_number
                runs_scored = delivery_info['runs']['extras']

                extras_runs1.append((runs_scored))



    for delivery in deliveries2:
        for delivery_number, delivery_info in delivery.items():
            if delivery_info['runs']['extras'] > 0:
                over_and_ball_number = delivery_number
                runs_scored = delivery_info['runs']['extras']

                extras_runs2.append((runs_scored))

    s1 = len(extras_runs1)
    s2 = len(extras_runs2)

    difference = s2-s1


    return difference
