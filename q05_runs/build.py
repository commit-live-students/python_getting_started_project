# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    # Your code here
    count = data['innings'][0]['1st innings']['deliveries']
    runs=0

    for i in count:
        sub_list=i.values()
        if sub_list[0]['batsman'] == 'BB McCullum':
            if sub_list[0]['runs']['batsman'] > 0:
                runs = runs + sub_list[0]['runs']['batsman']

    return runs

no_of_delivery = BC_runs(data)
