# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
from pprint import pprint
# Your Solution Here
def deliveries_count(data=data):

    # Your code here
    deliveries=data['innings'][0]['1st innings']['deliveries']
    current_delivery=0
    count=0
    #print(deliveries)
    for delivery in deliveries:

        #current_delivery+=0.1
        #print(delivery)
        (k, v), = delivery.items()
        #print(v['batsman'])
        if v['batsman']=='RT Ponting':
            #print(v['batsman'])
            count+=1
            #print(count)




       # print(delivery[current_delivery]['batsman'])


    return count
#pprint(data)
#deliveries_count(data)
