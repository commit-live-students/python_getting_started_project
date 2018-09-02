# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    count=0
    for a in data['innings'][0]['1st innings']['deliveries']:
        for b in a.values():
            for c in b.items():
                if c[0]=='batsman':
                    if c[1]=='RT Ponting':
               # if c=='RT Ponting':
                        count=count+1
                        print(count)
    return count


