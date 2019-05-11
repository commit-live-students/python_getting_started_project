# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    
    # Write your code here
    runs = 0
    del_list = []
    del_list = data['innings'][0]['1st innings']['deliveries']
    count = 0
    del_dict = {}
    for i in del_list:
        del_dict = i
        for key, value in del_dict.items():
            if(value['batsman'] == 'BB McCullum'):
                runs += value['runs']['batsman']
    print(runs)
    return(runs) 




