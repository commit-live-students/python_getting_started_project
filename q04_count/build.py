# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    firstinn_data = data['innings'][0]['1st innings']['deliveries']
    balls_faced = 0
    for f in firstinn_data:
         if f.values()[0]['batsman']=='RT Ponting':
                balls_faced=balls_faced+1
    return balls_faced
