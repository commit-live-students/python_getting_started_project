# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    runs=0
    items=data['innings'][0]['1st innings']['deliveries']
    for i in range(0,len(items)):
        if(items[i][items[i].keys()[0]]['batsman']=='BB McCullum'):
            runs=runs+items[i][items[i].keys()[0]]['runs']['batsman']





    return(runs)
