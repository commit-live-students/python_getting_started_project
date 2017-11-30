# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    inn = data["innings"][0]["1st innings"]["deliveries"]
    runs=0
    for i in range (0,len(inn)):
        delv = inn[i]
        if delv[delv.keys()[0]]['batsman'] == 'BB McCullum':
            runs=runs+delv[delv.keys()[0]]['runs']['batsman']
    return(runs)
