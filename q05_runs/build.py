# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data = data):
    runs=0
    for j in data['innings'][0]['1st innings']['deliveries']:
        for y,x in j.items():
            if x['batsman']== 'BB McCullum':
                runs=runs+x['runs']['batsman']
    return runs

    # Write your code here


    return(runs)
