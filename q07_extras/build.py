# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    extras_innings1 = []
    extras_innings2 = []
    
    list_deliveries1= data['innings'][0]['1st innings']['deliveries']
    list_deliveries2= data['innings'][1]['2nd innings']['deliveries']
    
    for delivery in list_deliveries1:
        for ballno,info in delivery.items():
            for key,runinfo in info.items():
                if key == 'extras':
                    extras_innings1.append(runinfo)
                
    for delivery in list_deliveries2:
        for ballno,info in delivery.items():
            for key,runinfo in info.items():
                if key == 'extras':
                    extras_innings2.append(runinfo)
    

    
    count_innings1=0
    for extras1 in extras_innings1:
        for key1,value1 in extras1.items():
            count_innings1+=value1
            
            
    count_innings2=0
    for extras2 in extras_innings2:
        for key2,value2 in extras2.items():
            count_innings2 += value2

    difference = abs(count_innings1 - count_innings2)


    return difference


