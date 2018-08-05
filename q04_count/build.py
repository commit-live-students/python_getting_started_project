# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

def deliveries_count(count):
    
    # Your code here
    count = 0
    x1 = data['innings']
    x2 = x1[0]
    x3 = x2['1st innings']['deliveries']
    
    for index, x in enumerate(x3):
        x4 = x3[index]
        for values in x4.values():
            if values['batsman'] == 'RT Ponting':
                count = count + 1
    return count



