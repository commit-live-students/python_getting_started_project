# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    count=0
    for k in data['innings'][0]['1st innings']['deliveries']:
        for y,x in k.items():
            if x['batsman']== 'RT Ponting':
                count=count+1
    return count
#data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']
'''for i in range(0,20):
    if i+0.7==True:
        ball=7
    else:
         ball=6
    for j in range(1,ball):
        a=i+(j/10)
        z=0
        z=z+1
        rtp=data['innings'][0]['1st innings']['deliveries'][z][a]['batsman']
        if rtp == 'RT Ponting':
            count=count+1
            print count'''
