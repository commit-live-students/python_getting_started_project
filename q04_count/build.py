# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution Here
def deliveries_count(data=data):
    
    # Your code here
    number_of_bowl = len(data['innings'][0]['1st innings']['deliveries']) #no of ball in 1st innings
    count = 0 #to count the number of ball RT pointing played
    
    for ball_no in range(number_of_bowl): #loop over each ball
    
        #return dictionary of particular ball no
        di = data['innings'][0]['1st innings']['deliveries'][ball_no]
        
        for ke  in di.keys():
            if data['innings'][0]['1st innings']['deliveries'][ball_no][ke]['batsman'] == 'RT Ponting':
                count = count + 1
    print(type(count))

    return count

deliveries_count()
         





