# %load q04_count/build.py
# Default Imports
import yaml
import json
import pandas as pd
from pandas.io.json import json_normalize
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
# with open(data, 'r') as f:
#     df = pd.io.json.json_normalize(yaml.load(f))

# print(df.head())
# Your Solution Here
def deliveries_count(data=data):
    
    # Your code here
    count=0
    s='SC Ganguly'
    name=data['innings'][0]['1st innings']['deliveries']
#     b1=name[0][0.1]['batsman']
#     df=pd.DataFrame
#     df=name
#     print(df)
    for delivery in name:
        for delivery_number,delivery_info in delivery.items():
            if delivery_info['batsman']=='RT Ponting':
                count+=1
    return count
deliveries_count(data)

