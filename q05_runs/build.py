# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    runs = 0
    first_inning = data['innings'][0]['1st innings']['deliveries']
    for each_delivery in first_inning:
        for each_ball, each_ball_detail in each_delivery.items():
            if each_ball_detail['batsman'] == 'BB McCullum':
                runs += each_ball_detail['runs']['batsman']

    return(runs)
BC_runs(data)
