# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):


    # Write your code here
    innings1 = data['innings'][0]['1st innings']['deliveries']
    innings2 = data['innings'][1]['2nd innings']['deliveries']
    extra_1 = 0
    extra_2 = 0
    for balls in innings1:
        for ball in balls.values():
            if ball['runs']['extras']!=0:
                extra_1+=1

    for balls in innings2:
        for ball in balls.values():
            if ball['runs']['extras']!=0:
                extra_2+=1



    difference = extra_2 - extra_1


    return difference
