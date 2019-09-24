# Default Imports
import yaml
import numpy as np
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):

    
    count = 0

    r = data['innings'][0]['1st innings']['deliveries']
    for d in r:
        for read_inside in d:
             if d[read_inside]['batsman'] == 'RT Ponting':
                 count += 1

    return count
