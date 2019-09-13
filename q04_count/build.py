# %load q04_count/build.py
# Default Imports
import pandas as pd
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    count = 0
    # Your code here
    first_inning = data['innings'][0]['1st innings']['deliveries']
    #return pd.DataFrame(first_inning)
    for each_delivery in first_inning:
        for each_ball, each_ball_detail in each_delivery.items():
            if each_ball_detail['batsman'] == 'RT Ponting':
                count+=1
    return count

deliveries_count(data)
