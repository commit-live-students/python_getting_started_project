# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    count=0
    
    # Your code here
    played_ball = {}
    for d in data['innings'][0]['1st innings']['deliveries']:
        for ball in d.keys():
            if(d[ball]['batsman'] == 'RT Ponting'):
                count += 1
            
            if(d[ball]['batsman'] in played_ball.keys()):
                played_ball[d[ball]['batsman']] += 1
            else:
                played_ball[d[ball]['batsman']] = 1


    return count

print(deliveries_count(data))



