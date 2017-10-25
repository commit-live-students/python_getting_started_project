# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    runs = 0
    delivs = data['innings'][0]['1st innings']['deliveries']
    for d in delivs:
        for ball_no, info in d.items():
            if info['batsman'] == 'BB McCullum':
                run_scored = info['runs']['batsman']
                runs += run_scored

    return runs
