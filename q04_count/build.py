# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):

    temp_1 = data.get('innings', {})
    temp_2 = temp_1[0]['1st innings']['deliveries']
    
    count = 0
    for t in temp_2:
        for s in t:
             if t[s]['batsman']=='RT Ponting':
                count = count + 1


    return count


deliveries_count()



