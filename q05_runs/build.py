# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data=data):

    # Write your code here
    runs = 0
    deliveries = data['innings'][0]['1st innings']['deliveries']
    for balls in deliveries:
        for x in balls:
            if balls[x]['batsman']=='BB McCullum':
                runs+=balls[x]['runs']['batsman']
                
    return(runs)

print(BC_runs())


