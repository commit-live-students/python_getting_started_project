from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
def first_batsman(data=data):
    opener_find1=data['innings']
    opener_find2=opener_find1[0]
    opener_find3=opener_find2['1st innings']['deliveries']
    opener_find4=opener_find3[0][0.1]
    name=opener_find4['batsman']
    return name
