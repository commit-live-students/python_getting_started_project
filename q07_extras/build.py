from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

def extras_runs(data=data):
    extras1=0
    extras2 =0 
    extras_first = data['innings'][0]['1st innings']['deliveries']
    extras_second = data['innings'][1]['2nd innings']['deliveries']
    for i in extras_first:
        for key, value in i.items():
            if('extras' in value.keys()):
                extras1 += 1
    for j in extras_second:
        for key, value in j.items():
            if('extras' in value.keys()):
                extras2 += 1
    
    difference = extras1-extras2
    #print(extras1, extras2)
    return abs(difference)

extras_runs()
        
    

