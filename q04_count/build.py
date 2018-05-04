from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
def deliveries_count(data=data):
    count=0
    deliveries = data['innings'][0]['1st innings']['deliveries']
    ponting_list=[]
    for delivery in deliveries:
        delivery_t = list(delivery.values())
        if delivery_t[0]['batsman']=='RT Ponting':
            count=count+1
    return count
deliveries_count(data)


