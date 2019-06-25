# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    runs=0
    run_by_McCullum=0
    l1 = data.get('innings')[0].get('1st innings').get('deliveries')
    for s in l1:
        for key, value in s.items():
            myval = value
            name=str(myval.get('batsman'))         
            if(name=='BB McCullum'):
                run_by_McCullum=myval.get('runs').get('batsman')
                runs = runs+run_by_McCullum

    return(runs)

BC_runs(data)


