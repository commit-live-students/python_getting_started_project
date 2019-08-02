# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    innings1 = data['innings'][0]['1st innings']['deliveries']
    innings2 = data['innings'][1]['2nd innings']['deliveries']
    in1 = 0
    in2 = 0
    i = 0
    ls = [innings1, innings2]
    for i in ls:
        for ball in i:
            for each_ball in ball.values():
                if 'extras' in each_ball.keys():
                    if i == innings1:
                        in1 += 1
                    else:
                        in2 += 1

    difference = abs(in1 - in2)

    return difference
