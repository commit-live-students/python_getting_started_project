# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


#print data.keys()
def first_batsman(data1):
    t2 = data1["innings"]
    #print t2
    y = t2[0]
    z = y.values()
    a = z[0]
    b = a['deliveries']
    c = b[0]
    d = c.values()
    e = d[0]
    variable = e['batsman']
    return variable

print first_batsman(data)
