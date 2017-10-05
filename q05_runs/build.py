# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
    # Write your code here
run=[]
def BC_runs(data=data):

    # write your code here
    teams=data['innings'] [0] ['1st innings']['deliveries']
    for t in teams:
        for i in t:
            if t[i]['batsman']=='BB McCullum' :
                a=t[i]['runs']['batsman']
                run.append(a)
    runs=sum(run)
    print (runs)
    return(runs)
