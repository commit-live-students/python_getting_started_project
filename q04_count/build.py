# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    count=data['innings'][0]['1st innings']['deliveries']
    no_of_runs=0
    for n in count:
        if n.values()[0]['batsman']=='RT Ponting':
            no_of_runs=no_of_runs+1
    return no_of_runs
