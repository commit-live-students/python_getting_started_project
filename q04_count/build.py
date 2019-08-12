from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
def deliveries_count(data=data):
            subset_data = data['innings'][0]['1st innings']['deliveries']
            nos_of_delivery = 0
            for i in subset_data:
                        if i.values()[0]['batsman']=='RT Ponting':
                                    nos_of_delivery=nos_of_delivery+1
            #print nos_of_delivery
            return nos_of_delivery
deliveries_count(data)
