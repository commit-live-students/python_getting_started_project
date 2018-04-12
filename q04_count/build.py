# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    
    # Your code here
    count=0
    lst1=data['innings'][0]['1st innings']['deliveries']
    for lst in lst1:
        ball_detail=lst
        for ball_number in ball_detail.keys():
            if(ball_detail[ball_number]['batsman']=='RT Ponting'):
                count+=1
    return count
deliveries_count(data)

