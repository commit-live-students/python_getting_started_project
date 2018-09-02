def BC_runs (matchDetails) :
    runs=0
    if(len(matchDetails)>0) :
        for index,delInfo in enumerate(matchDetails['innings'][0]['1st innings']['deliveries']) :
            for key,value in delInfo.items() :
                if value['batsman'] == 'BB McCullum' :
                    runsScored=value['runs']['batsman']
                    runs+=runsScored
    return runs;





