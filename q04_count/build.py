# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
# Your Solution Here
def deliveries_count(data=data):
    count=0
    l1 = data.get('innings')[0].get('1st innings').get('deliveries')
    for s in l1:
        for key, value in s.items():
            myval = value
            name=str(myval.get('batsman'))         
            if(name=='RT Ponting'):
                count = count+1

    return count


