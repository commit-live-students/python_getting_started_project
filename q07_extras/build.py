# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    first_extras = 0
    first_inning = data['innings'][0]['1st innings']['deliveries']
    for each_delivery in first_inning:
        for each_ball, each_ball_detail in each_delivery.items():
            #print each_ball_detail['runs']['extras']
            if each_ball_detail['runs']['extras'] > 0:
                first_extras += 1
    #print first_extras
    second_extras = 0
    second_inning = data['innings'][1]['2nd innings']['deliveries']
    for each_delivery in second_inning:
        for each_ball, each_ball_detail in each_delivery.items():
            if each_ball_detail['runs']['extras'] > 0:
                second_extras += 1
    difference = abs(second_extras - first_extras)


    return difference
extras_runs(data)
