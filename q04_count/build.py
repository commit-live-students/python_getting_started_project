# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):

    # Your code here
    count = 0

    data = data['innings']

    data = [i['1st innings'] for i in data if '1st innings' in i]

    data = [i['deliveries'] for i in data if 'deliveries' in i]

    for l in data[0]:
        for i in l:
            if l[i]['batsman'] == 'RT Ponting':
                count += 1

    return count
