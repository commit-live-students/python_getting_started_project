# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
first_innings = []
second_innings = []



# Your Solution
def extras_runs(data=data):
    first_deliveries = data['innings'][0]['1st innings']['deliveries']
    for delivery in first_deliveries:
        for deliver_key, deliver_val in delivery.items():
            if 'extras' in deliver_val:
                counter = 1
                first_innings.append(counter)
    extra_first = sum(first_innings)

    second_deliveries = data['innings'][1]['2nd innings']['deliveries']
    for delivery in second_deliveries:
        for deliver_key, deliver_val in delivery.items():
            if 'extras' in deliver_val:
                counter = 1
                second_innings.append(counter)
    extra_second = sum(second_innings)

    difference = extra_second - extra_first

    return difference
