# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


            
# Your Solution Here
def deliveries_count(data=data):
    
    # Your code here
    count = 0 
    
    # get the decitionary about first innnings delieveries in dictionary balls
    balls = data['innings'][0]['1st innings']['deliveries']
    
    #iterate throgh each ball and get the value of each batsman
    for bal in balls:
        for btmn in bal.values() :
            if  btmn['batsman'] == 'RT Ponting':
                count += 1
            else:
                pass
    return count


if __name__ == '__main__':
    deliveries_count()
    print(deliveries_count())



