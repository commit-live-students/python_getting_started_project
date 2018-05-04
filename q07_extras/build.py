
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

def extras_runs(data=data):

    extras1=0
    extras2=0
    difference = 0
    
    #for innings 1
    maintemp = (data['innings'][0]['1st innings']['deliveries'])
    len_maintemp = len(maintemp)
    
    for ctr in range(len_maintemp):
        temp_balls=(list(maintemp[ctr]))
        balls=float(temp_balls[0])
        
        if 'extras' in maintemp[ctr][balls]:
            #extras1+=maintemp[ctr][balls]['runs']['extras']
            extras1+=1
            #print(extras1)
    
    #for innings 2
    maintemp2 = (data['innings'][1]['2nd innings']['deliveries'])
    len_maintemp2 = len(maintemp2)
    
    for deli in range(len_maintemp2):
        temp_balls=(list(maintemp2[deli]))
        balls=float(temp_balls[0])
        
        if 'extras' in maintemp2[deli][balls]:
            extras2+=1
            
    difference=extras2-extras1
    return difference
extras_runs(data)


