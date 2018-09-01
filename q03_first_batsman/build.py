
def first_batsman(matchDetails) :
    first_batsman_name=''
    if(len(matchDetails)>0) :
        first_batsman_name=matchDetails['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']
    return first_batsman_name

        






