# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    
    # Your code here
    total_balls = len(data['innings'][0]['1st innings']['deliveries'])
    count = 0
    for i in range(0,total_balls):
        key = next(iter(data['innings'][0]['1st innings']['deliveries'][i]))
        if data['innings'][0]['1st innings']['deliveries'][i][key]['batsman']=='RT Ponting':
            count = count+1
    return count




