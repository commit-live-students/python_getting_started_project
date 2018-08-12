# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

from pprint import pprint
# Your Solution
def extras_runs(data=data):

    # Write your code here
    first_inn_run=0
    second_inn_run=0
    second_inning=data['innings'][1]['2nd innings']['deliveries']
    first_inning=data['innings'][0]['1st innings']['deliveries']


    for delivery in second_inning:
        (k, v), = delivery.items()

        if(v.get('extras')!=None):
            first_inn_run+=1

    print(first_inn_run)

    for delivery in first_inning:
        (k, v), = delivery.items()

        if(v.get('extras')!=None):
            second_inn_run+=1

    #print(second_inn_run)

    difference =first_inn_run-second_inn_run


    return difference

#extras_runs(data)
#pprint(data)
