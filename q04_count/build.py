# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):

    # Your code here
    count = 0
    for innings in data['innings']:
        for inning in innings:
            for delivery in innings[inning]['deliveries']:
                delivery_content = delivery[next(iter(delivery))]
                batsman = delivery_content['batsman']
                if (batsman == 'RT Ponting'):
                    count += delivery_content['runs']['batsman']

    return count
