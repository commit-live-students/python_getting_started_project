# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    deliveries_1st = data['innings'][0]['1st innings']['deliveries']
    runs = 0
    for i in deliveries_1st:   
        for key in i:
            if(i[key]['batsman']=='BB McCullum'):
                #print(i[key]['batsman'])
                runs += i[key]['runs']['batsman']

    return runs

BC_runs(data)


