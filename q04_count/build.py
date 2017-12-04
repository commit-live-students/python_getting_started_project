# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):

    # Your code here
    count = 0
    dely = data['innings'][0]['1st innings']['deliveries']
    loop_var = 0
    for batsman in dely:
        ind = data['innings'][0]['1st innings']['deliveries'][loop_var].keys()
        batsman = data['innings'][0]['1st innings']['deliveries'][loop_var][ind[0]]['batsman']
        if batsman == 'RT Ponting':
            count=count + 1
        loop_var=loop_var + 1

    return count

print deliveries_count()
