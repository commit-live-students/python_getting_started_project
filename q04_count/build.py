# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data

import pandas as pd
import numpy as np


data = read_data()
count=0
ball_faced=[0]
# Your Solution Here
def deliveries_count(data=data):
    count=0
    list_deliveries= data['innings'][0]['1st innings']['deliveries']
    for delivery in list_deliveries:
        for delivery_number, delivery_info in delivery.items():
            if delivery_info['batsman'] == 'RT Ponting':
                count += 1

    return count
    
    
    
    
                 
    # Your code here



