# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    
    # Your code here
    count = 0
    firstinn = data['innings'][0]['1st innings']['deliveries']
    for deliv in firstinn:
        for key in deliv:
            if deliv[key]['batsman'] == 'RT Ponting':
                count+=1
    return count


