# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
difference = 0


# Your Solution
def extras_runs(data=data):
    
    extras1 = 0
    extras2 = 0
    # Write your code here
    balls_1 = data['innings'][0]['1st innings']['deliveries']
    
    for bal in balls_1:
        for extra in bal.values():
            if extra['runs']['extras'] >0:
                extras1 += 1


    balls_2 = data['innings'][1]['2nd innings']['deliveries']
    extras2 = 0
    for bal in balls_2:
        for extra in bal.values():
            if extra['runs']['extras'] >0:
                extras2 += 1


    difference = extras2 - extras1


    return difference


if __name__ == '__main__':
    extras_runs()
    print(extras_runs())


