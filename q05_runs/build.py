# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    # Write your code here
    runs=0
    lst1=data['innings'][0]['1st innings']['deliveries']
    for lst in lst1:
        ball_detail=lst
        for ball_number in ball_detail.keys():
            if(ball_detail[ball_number]['batsman']=='BB McCullum'):
                if (ball_detail[ball_number]['runs']['batsman']!= 0):
                    runs+=ball_detail[ball_number]['runs']['batsman']
    return(runs)




