#%load q03_first_batsman/build.py

import yaml

def first_batsman(d):
    data=open('./data/ipl_match.yaml','r')
    data1=yaml.load(data)
    data2=data1['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']
#data3=data2['1st innings']['deliveries'][0][0.1]['batsman']
#print(data3)
    return data2

    







