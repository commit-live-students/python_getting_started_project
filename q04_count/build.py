# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    count=0
    # Your code here
    test=data['innings'][0]['1st innings']['deliveries']

    for i in range(len(test)):

        for j in test[i].values():

            if(j['batsman']=='RT Ponting'):
                print(j)
                count+=1
    return count
