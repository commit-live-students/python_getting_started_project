# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

bowled_players=[]
# Your Solution
def bowled_out(data=data):
    #bowled_players=[]
    ing=data.get('innings')
    firsting=ing[1]
    fingdict=firsting.get('2nd innings')
    deliveries=fingdict.get('deliveries')
    for ball in deliveries:
        bat=list(ball.values())
        if ((bat[0].get('wicket'))!=None):
            wicket=bat[0].get('wicket')
            if(wicket.get('kind')=='bowled'):
                player=wicket.get('player_out')
                bowled_players.append(player)
                

    # Write your code here


    return bowled_players




