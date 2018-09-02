from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

def extras_runs(data=data):
    l1 = []
    l2 = []
    d1 = list(data['innings'][0]['1st innings']['deliveries'])
    d2 = list(data['innings'][1]['2nd innings']['deliveries'])
    #extras in first innings
    for index, value in enumerate(d1):
        for key in value:
            try:
                l1.append(value[key]['extras'])
            except:
                continue
                
    #extras in second innings        
    
    for index, value1 in enumerate(d2):
        for key in value1:
            try:
                l2.append(value1[key]['extras'])
            except:
                continue
            
    difference = len(l2) - len(l1)
    return difference

from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
l1 = []
l2 = []
d2 = list(data['innings'][1]['2nd innings']['deliveries'])
for index, value in enumerate(d2):
    for key in value:
        try:
            l1.append(value[key]['extras'])
        except:
            continue
print(l1)
len(l1)

                    
            
            




