# %load q04_count/build.py
# Default Imports
from pprint import pprint
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
#count=0
#pprint(data['innings'][0]['1st innings']['deliveries'])
# Your Solution Here
'''deliveries_lst=data['innings'][0]['1st innings']['deliveries']
for ball in deliveries_lst:
    value_per_ball=ball.values()
    batsman=value_per_ball[0]['batsman']
    if batsman=="RT Ponting":
        print(value_per_ball[0]['batsman'])
        #runs=value_per_ball
        count=count+1
print(count)'''
    #ballno=data['innings'][0]['1st innings']['deliveries'][0]
   # print(ballno)
def deliveries_count(data=data):
    count=0
    deliveries_lst=data['innings'][0]['1st innings']['deliveries']
    for ball in deliveries_lst:
        value_per_ball=ball.values()
        batsman=value_per_ball[0]['batsman']
        if batsman=="RT Ponting":
            #print(value_per_ball[0]['batsman'])
        #runs=value_per_ball
            count=count+1


    # Your code here


    return count
#cnt=deliveries_count(data)
#print(cnt)
