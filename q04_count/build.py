from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
find1=data['innings']
find2=find1[0]
find3=find2['1st innings']['deliveries']
def deliveries_count(data=data):
    nos_of_delivery = 0
    for i in find3:
        if i.values()[0]['batsman']=='RT Ponting':
            nos_of_delivery = nos_of_delivery + 1
    return nos_of_delivery
