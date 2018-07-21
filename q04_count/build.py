# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    
    # Your code here
    count=0
    overs_balls=data['innings'][0]['1st innings']['deliveries']
    #print(overs_balls)
    #print(len(overs_balls))
    for i in range(len(overs_balls)):
        for key in overs_balls[i]:
            if overs_balls[i][key]['batsman']=='RT Ponting':
                count+=1
    return count

deliveries_count(data)



