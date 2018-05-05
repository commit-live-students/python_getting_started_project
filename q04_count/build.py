from greyatomlib.python_getting_started.q01_read_data.build import read_data

data = read_data()

def deliveries_count(data=data):
    count=0
    deliveries = data['innings'][0]['1st innings']['deliveries']
    b = 0.1
    for a in range(len(deliveries)):
        for b in deliveries[a]:
            if (deliveries[a][b]['batsman']=='RT Ponting'):
                count+=1
    return count
    
deliveries_count()


