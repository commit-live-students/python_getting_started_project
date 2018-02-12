# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


def deliveries_count(data=data):
    count =0
    deliveries=data['innings'][0]['1st innings']['deliveries']
    for deliveries in deliveries:
        for rounds in deliveries:
            if deliveries[rounds].get('batsman')== 'RT Ponting':
                batsman=deliveries[rounds].get('batsman')
                count += 1
    print count
    return count
