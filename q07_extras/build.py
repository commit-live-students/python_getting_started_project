# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    inning_1_extras = 0
    for balls in data['innings'][0]['1st innings']['deliveries']:
        for ball in balls:
            if balls[ball]['runs']['extras'] != 0 :
                inning_1_extras = inning_1_extras + 1
    inning_2_extras = 0
    for balls in data['innings'][1]['2nd innings']['deliveries']:
        for ball in balls:
            if balls[ball]['runs']['extras'] != 0 :
                inning_2_extras = inning_2_extras + 1
    difference = inning_1_extras - inning_2_extras
    return abs(difference)
