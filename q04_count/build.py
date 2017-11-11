# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):

    # Your code here
    d = data['innings'][0]['1st innings']['deliveries']
    count = len([k for a in d for k in a if a[k]['batsman'] == 'RT Ponting'])
    return count
