from greyatomlib.python_getting_started.q01_read_data.build import read_data

data = read_data()

def first_batsman(data=data):

    name=data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']
    return name

first_batsman()
read_data()

