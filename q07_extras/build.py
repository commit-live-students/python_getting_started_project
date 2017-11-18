# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
# Your Solution
def extras_runs(data=data):
    # Write your code here
    difference = inning_extras ('2nd innings',1) - inning_extras ('1st innings',0)
    return difference


def inning_extras (inning, inning_index):
    count =0
    for deliveries in data['innings'][inning_index][inning]['deliveries']:
        for delivery in deliveries:
            if 'extras' in deliveries[delivery]:
                count = count +1
    return count
