# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    runs=0
    for a in data['innings'][0]['1st innings']['deliveries']:
            for b in a.values():
                if b['batsman']=='BB McCullum':
                   for c in b.values():
                        if isinstance(c,dict) and len(c)==3:
         #       if c[0]=='batsman':
          #           if c[1]=='BB McCullum':
                         #print(c['batsman'])
                         runs=runs+c['batsman']
                        # print(runs)
                        
    return(runs)



