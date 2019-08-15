# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    runs = 0
    req_data = data['innings'][0]['1st innings']['deliveries']
    for i in req_data:
        overs = i.items()
        for ball in overs:
            if ball[1]['batsman'] == 'BB McCullum':
                runs += ball[1]['runs']['batsman']

    return(runs)
