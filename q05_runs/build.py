# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


def BC_runs(data):
    runs = 0
    delivery = data['innings'][0]['1st innings']['deliveries']
    for i in delivery:
        for key in i:
            if i[key]['batsman']=='BB McCullum':
                runs+=i[key]['runs']['batsman']
    return(runs)




