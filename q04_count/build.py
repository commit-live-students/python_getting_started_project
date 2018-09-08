# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    ing=data.get('innings')
    firsting=ing[0]
    fingdict=firsting.get('1st innings')
    deliveries=fingdict.get('deliveries')
    count=0
    for ball in deliveries:
        bat=list(ball.values())
        if bat[0].get('batsman')=='RT Ponting':
            count=count+1
            
    # Your code here
    

    return count

deliveries_count(data)


