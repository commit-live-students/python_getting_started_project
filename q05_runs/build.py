# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    runs=0
    delivery=data['innings'][0]['1st innings']['deliveries']
    for index in range(len(delivery)):
        for key in delivery[index]:
            if(delivery[index][key]['batsman']=='BB McCullum'):
                runs += delivery[index][key]['runs']['batsman']

    return(runs)


