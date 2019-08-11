# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
def deliveries_count(data=data):
    find1=data['innings']
    find2=find1[0]
    find3=find2['1st innings']['deliveries']
    count = 0
    for i in find3:
            if i.values()[0]['batsman']=='RT Ponting':
                count=count+1
    return count
