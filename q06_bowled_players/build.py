# %load q06_bowled_players/build.py
# Default Imports
from pprint import pprint
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

#pprint(data['innings'][1]['2nd innings']['deliveries'])
'''
balls_list=data['innings'][1]['2nd innings']['deliveries']
pprint(balls_list)
bowled_players=0
for ball in balls_list:
    val=ball.values()
    #pprint(val[0])
    if 'wicket' in val[0]:
        #pprint("yes")
        kind=val[0]['wicket']['kind']
        #pprint(kind)
        if kind=='bowled':
            #pprint('yes')
            bowled_players=bowled_players+1
pprint(bowled_players)
'''


# Your Solution
def bowled_out(data=data):
    balls_list=data['innings'][1]['2nd innings']['deliveries']
    bowled_players=[]
    for ball in balls_list:
        val=ball.values()
    #pprint(val[0])

        if 'wicket' in val[0]:
        #pprint("yes")
            kind=val[0]['wicket']['kind']
        #pprint(kind)
            if kind=='bowled':
            #pprint('yes')
                bowled_players.append(val[0]['batsman'])
#pprint(bowled_players)


    # Write your code here


    return bowled_players
