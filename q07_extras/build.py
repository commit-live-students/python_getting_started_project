# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    extras_1 = []
    extras_2 = []
    for d in data['innings'][1]['2nd innings']['deliveries']:
        for k, v in d.items():
            if v['runs']['extras'] > 0:
                extras_2.append(v['runs']['extras'])
    for d in data['innings'][0]['1st innings']['deliveries']:
        for k, v in d.items():
            if v['runs']['extras'] > 0:
                extras_1.append(v['runs']['extras']) 

    difference = len(extras_2) - len(extras_1)

    return difference

extras_runs(data)
