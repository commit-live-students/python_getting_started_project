# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
#import yaml
#count = 0
#with open('../data/ipl_match.yaml') as f:
    #data = yaml.load(f)
data = read_data()

#print data

# Your Solution Here
def deliveries_count(data=data):
    count = 0
    for i in range (len(data['innings'][0]['1st innings']['deliveries'])):
        a = data['innings'][0]['1st innings']['deliveries'][i].values()
        if (a[0]['batsman']) == "RT Ponting":
            count = count+1
            print count

    return count
deliveries_count()
