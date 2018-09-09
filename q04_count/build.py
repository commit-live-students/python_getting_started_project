from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


def deliveries_count(data=data):
    count=0
    d = list(data['innings'][0]['1st innings']['deliveries']) 
    for index, value in enumerate(d):
        for key in value:
            if value[key]['batsman'] == 'RT Ponting':
                count+= 1
        else:
            continue
            
            
                
        
        
    
    return count

data = read_data()
d = list(data['innings'][0]['1st innings']['deliveries'])
d[0]



