# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

def bowled_out(data):
    list_1st_inn = data["innings"]
    #print list_1st_inn
    deliveries_second =  list_1st_inn[1]["2nd innings"]["deliveries"]
    #print deliveries_second
    bowled_players = []

    for d in deliveries_second:
        for e in d.values():
            #print e.keys()
            for x in e.keys():
                #print x

                if(x == "wicket"):
                    n = e.values()[4]

                    if(n["kind"] == 'bowled'):
                        y = n.get('player_out')
                        bowled_players = bowled_players + [y]
    return bowled_players



print bowled_out(data)
    
