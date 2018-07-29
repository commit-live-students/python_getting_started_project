# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    a=data['innings'][0]['1st innings']['deliveries']
    runs=0
    # Write your code here
    
    for i in range(len(a)):
        for j in a[i].values():
            if j['batsman']=='BB McCullum':
                for k in j['runs'].items():
                    if k[0]=='batsman':
                        runs=runs+k[1]
    return runs

    

c=BC_runs(data)
c


