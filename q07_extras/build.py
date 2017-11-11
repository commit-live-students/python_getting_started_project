# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
        # Write your code here
    difference = 0
    for i in range(len(data['innings'])):
        for key in data['innings'][i]:
            for delivery_number in data['innings'][i][key]['deliveries']:
                if 'extras' in delivery_number.values()[0]:
                    for extra in delivery_number.values()[0]['extras']:
                        if i % 2 == 0:
                            difference -= len(delivery_number.values()[0]['extras'].keys())
                        else:
                            difference += len(delivery_number.values()[0]['extras'].keys())


    return abs(difference)
