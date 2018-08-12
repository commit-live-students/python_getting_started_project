# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):

    # write your code here
    teams=data['innings'] [0] ['1st innings']['deliveries']
    count=0
    for t in teams:
        for i in t:
            if t[i]['batsman']=='RT Ponting' :
               count+=1
    return count

deliveries_count()
