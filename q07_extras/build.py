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
                first_inning_extra = deliver_val['runs']['extras']
                first_innings.append (first_inning_extra)
    extra_first = sum(first_innings)
    second_deliveries = data['innings'][1]['2nd innings']['deliveries']
    for delivery in second_deliveries:
        for deliver_key, deliver_val in delivery.items():
                second_inning_extra = deliver_val['runs']['extras']
                second_innings.append (second_inning_extra)
    extra_second = sum(second_innings)

    difference = extra_second - extra_first

    return difference
