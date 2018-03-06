# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
ganguly_runs = []
def deliveries_count(data=data):
    count = data['innings'][0]['1st innings']['deliveries']
    for delivery in count:
        for delivery_number, delivery_info in delivery.items():
            if delivery_info['batsman'] == 'SC Ganguly':
                over_and_ball_number = delivery_number
                runs_scored = delivery_info['runs']['batsman']

                ganguly_runs.append((over_and_ball_number, runs_scored))


    return count
print deliveries_count()
