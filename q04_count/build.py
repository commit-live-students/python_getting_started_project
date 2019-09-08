# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    count = 0
    a = data['innings'][0]['1st innings']['deliveries']
    for i in range(len(a)):
        for k in a[i]:
            if a[i][k]['batsman'] == 'RT Ponting':
                count += a[i][k]['runs']['batsman']

    # Your code here


    return count
