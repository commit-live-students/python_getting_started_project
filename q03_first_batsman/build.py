# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
import pprint
data = read_data()
name="hello"

# Your Solution
def first_batsman(data=data):
    deliveries = data['innings'][0]['1st innings']['deliveries'][0]
    for key,val in deliveries.items():
        if(key == 0.1):
            global name
            name= val['batsman']
            break
    return name
first_batsman(data)
