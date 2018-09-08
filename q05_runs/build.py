# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    ing=data.get('innings')
    firsting=ing[0]
    fingdict=firsting.get('1st innings')
    deliveries=fingdict.get('deliveries')
    runs=0
    for ball in deliveries:
        bat=list(ball.values())
        if bat[0].get('batsman')=='BB McCullum':
            run=bat[0].get('runs').get('batsman')
            runs=runs+run

    # Write your code here


    return(runs)

BC_runs(data)

