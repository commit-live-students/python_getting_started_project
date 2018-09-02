def getExtraBowled(matchDetailsList) :
    extra=0
    for index,delInfo in enumerate(matchDetailsList) :
        for key,value in delInfo.items() :
            if 'extras' in value:
                if 'wides' in value['extras']:
                    extra=extra+1
                        
    return extra
    
    
def extras_runs(matchDetails) :
    one_extras=0
    sec_extras=0
    if(len(matchDetails)>0) :
        one_extras=getExtraBowled(matchDetails['innings'][0]['1st innings']['deliveries'])
        sec_extras=getExtraBowled(matchDetails['innings'][1]['2nd innings']['deliveries'])
       
    return sec_extras-one_extras

