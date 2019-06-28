# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    runs=0
    overs_balls=data['innings'][0]['1st innings']['deliveries']
    for i in range(len(overs_balls)):
        for key in overs_balls[i]:
            if overs_balls[i][key]['batsman']=='BB McCullum':
                runs+=overs_balls[i][key]['runs']['batsman']

    return(runs)

BC_runs(data)



