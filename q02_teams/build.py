# default imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


def teams(data1):
    variable1 = data1["info"]
    variable = variable1["teams"]
    return variable

print teams(data)
