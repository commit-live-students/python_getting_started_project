# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def first_batsman(data=data):

    # Write your code here
    dd = data['innings'][0]['1st innings']['deliveries'][0]
    for values in dd.values():
        name=values['batsman']



    return name
