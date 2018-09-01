
def deliveries_count (matchDetails) :
    count=0
    if(len(matchDetails)>0) :
        for index,delInfo in enumerate(matchDetails['innings'][0]['1st innings']['deliveries']) :
            for key,value in delInfo.items() :
                if value['batsman'] == 'RT Ponting' :
                    count=count+1
                    print(value)
                    
    return count;
            




