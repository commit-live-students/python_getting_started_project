# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
def deliveries_count(data=data):
    d = data['innings'][0]['1st innings']['deliveries']
    n = 0
    count = 0
    while n <= 123:
        ls = d[n]
        for k in ls:
            nw = ls[k]
            for s in nw:
                nm = nw['batsman']
        if nm == 'RT Ponting':
            count = count + 1
    n = n + 1
    return count
print count
