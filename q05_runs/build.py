# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    runs=0
    test=data['innings'][0]['1st innings']['deliveries']
    #print(test)
    for i in range(len(test)):
        for j in test[i].values():
            #print (j)
            if(j['batsman']=='BB McCullum'):
                runs+=j['runs']['batsman']

    return(runs)

BC_runs(data)
