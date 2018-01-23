# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(*data=data):
    count = 0
    for n in data:
        count += 1

    # Your code here


    return count
