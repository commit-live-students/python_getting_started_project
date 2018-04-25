# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    runs=0
    for e in data['innings'][0]['1st innings']['deliveries']:
        for key,element in e.items():
            if e[key]['batsman']=='BB McCullum':
                runs=runs+e[key]['runs']['batsman']
            


    return(runs)

#print(type(data['innings'][0]['1st innings']['deliveries']))
print(data['innings'][0]['1st innings']['deliveries'][0])

runs=0
for e in data['innings'][0]['1st innings']['deliveries']:
    for key,element in e.items():
        if e[key]['batsman']=='BB McCullum':
            runs=runs+e[key]['runs']['batsman']
            print(e[key]['batsman'],e[key]['runs']['batsman'],runs)



