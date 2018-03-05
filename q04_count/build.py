# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    count = 0
    innings_list = data['innings']
    firstinningdeliveries_list = innings_list[0]['1st innings']['deliveries']
    for i in range(0, len(firstinningdeliveries_list)):
        for k1, v1 in firstinningdeliveries_list[i].items():
            #print k1, ' -->>  ', v1
            if (v1['batsman'] == 'RT Ponting'):
                count += 1
                
    return count

print deliveries_count(data)
