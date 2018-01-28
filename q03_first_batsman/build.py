# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def first_batsman(data=data):
    # Write your code here
    for ele in data['innings'][0].values():
	       name =  ele['deliveries'][0][0.1]['batsman']

    return name
