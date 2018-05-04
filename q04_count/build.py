
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

def deliveries_count(data=data):
    count=0
    deli = (data['innings'][0]['1st innings']['deliveries'])
    deli_len = len(deli)
    
    for ctr in range(deli_len):
        temp_delivery=(list(deli[ctr]))
        delivery=float(temp_delivery[0])
       
        if deli[ctr][delivery]['batsman'] == 'RT Ponting':
                count+=1
    return count


deliveries_count()


