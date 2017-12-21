# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data1 = read_data()

def BC_runs(data):
    lst = data['innings'][0]['1st innings']['deliveries']

    run = 0
    for d in lst:
        balls = d.values()
        if balls[0]['batsman'] == 'BB McCullum':
            run += balls[0]['runs']['batsman']
    return run

BC_runs(data1)
