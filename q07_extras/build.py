# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
from pprint import pprint
# Your Solution
def extras_runs(data=data):

    # Write your code here
    #pprint(data['innings'][1]['2nd innings']['deliveries'])
    balls=data['innings'][1]

   # difference =

    first=extra(balls,0,'1st innings')
    second=extra(balls,1,'2nd innings')
    #pprint(first)
    #pprint(second)
    if second>first:
        difference =second-first
    else:
        difference =first-second
    return difference

def extra(balls,ind,inn):
    balls=data['innings'][ind][inn]['deliveries']
    #pprint(balls)
    #diff=0
    cnt2=0
    for ball in balls:
        val=ball.values()
        #pprint(val)
        if 'extras' in val[0]:
            cnt2=cnt2+1
            #print("yes")
    return cnt2



#d=extras_runs()
#print(d)
