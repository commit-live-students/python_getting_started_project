# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def first_batsman(data=data):

    # Write your code here
    from greyatomlib.python_getting_started.q01_read_data.build import read_data
    data = read_data()
    test =  data['innings'][0]['1st innings']
    test2 = test['deliveries'][0]
    test3 = test2[0.1]
    name = test3['batsman']
    return name
