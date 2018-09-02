# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
runs=0
def BC_runs(data):
    runs=0
    deliveries=data['innings'][0]['1st innings']['deliveries']
    for balls in deliveries:
        for k,v in balls.items():
            for p,q in v.items():
                if p=='batsman' and q=='BB McCullum':
                    for w,r in v['runs'].items():
                        if w=='batsman':
                            runs=runs+r
    return(runs)

runs=0
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
deliveries=data['innings'][0]['1st innings']['deliveries']
for balls in deliveries:
    for k,v in balls.items():
        for p,q in v.items():
            if p=='batsman' and q=='BB McCullum':
                for w,r in v['runs'].items():
                    if w=='batsman':
                        runs+=r
print (runs)
                        
        


