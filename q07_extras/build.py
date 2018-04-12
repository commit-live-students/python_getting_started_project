# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    extras_innings1=0
    extras_innings2=0
    lst1=data['innings'][0]['1st innings']['deliveries']
    for lsti1 in lst1:
        ball_detaili1=lsti1
        for ball_numberi1 in ball_detaili1.keys():
            extras_innings1+=ball_detaili1[ball_numberi1]['runs']['extras']
            
    lst2=data['innings'][1]['2nd innings']['deliveries']
    for lsti2 in lst2:
        ball_detaili2=lsti2
        for ball_numberi2 in ball_detaili2.keys():
            extras_innings2+=ball_detaili2[ball_numberi2]['runs']['extras']
    difference =(extras_innings2-extras_innings1)*3


    return difference

