# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    b = data['innings'][0]['1st innings']['deliveries']
    c = 0
    for i in b:
        for e in i.items():
            if e[1]['batsman'] == 'RT Ponting':
                c = c+1
    return c
deliveries_count(data)
#print(data)



