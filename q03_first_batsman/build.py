# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
def first_batsman(data=data):
    d = data['innings']
    f = d[0]
    g = f ['1st innings']
    h = g['deliveries'][0]
    i = h[0.1]
    name = i['batsman']
    print name
    return name
