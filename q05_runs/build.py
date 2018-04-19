# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data=data):
    count=0
    runs=0
    deliveries = data['innings'][0]['1st innings']['deliveries']
    b = 0.1
    for a in range(len(deliveries)):
        for b in deliveries[a]:
            print(deliveries[a][b]['runs']['batsman'])
            runs_= deliveries[a][b]['runs']['batsman']
            if (deliveries[a][b]['batsman']=='BB McCullum'):
                runs=runs+runs_
                count+=1
                print(runs)

    return runs
print(BC_runs())

    # Write your code here


   

