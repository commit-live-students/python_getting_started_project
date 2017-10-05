from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
def first_batsman(data=data):
    name = []
    s = data['innings'][0]['1st innings']['deliveries'][0]
    for key,value in s.items():
        name = value['batsman']
        return name
