def bowled_out(matchDetails) :
    bowled_players=[]
    if(len(matchDetails)>0) :
        for index,delInfo in enumerate(matchDetails['innings'][1]['2nd innings']['deliveries']) :
            for key,value in delInfo.items() :

                if 'wicket' in value :
                    if value['wicket']['kind'] == 'bowled' :
                        bowled_players.append(value['wicket']['player_out'])
             
    return bowled_players

