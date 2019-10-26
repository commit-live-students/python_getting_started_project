# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    first_innings_extras = 0
    second_innings_extras = 0

    for balls in data['innings'][0]['1st innings']['deliveries']:
        for key, value in balls.items():
            if 'extras' in value:
                first_innings_extras += 1

    for balls in data['innings'][1]['2nd innings']['deliveries']:
        for key, value in balls.items():
            if 'extras' in value:
                second_innings_extras += 1

    difference = second_innings_extras - first_innings_extras

    return difference
