# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    runs = 0
    del_list = data['innings'][0]['1st innings']['deliveries']
    for i in range(0, len(del_list)):
        for k1, v1 in del_list[i].items():
            if (v1['batsman'] == 'BB McCullum'):
                runbymc = v1['runs']['batsman']
                runs += runbymc

    return(runs)

print BC_runs(data)
