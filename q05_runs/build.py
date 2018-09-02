# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

run=0
# Your Solution
def BC_runs(data):
    rt=data['innings'][0]['1st innings']['deliveries']
    run=0
    for x in rt:
        for k,v in x.items():
            for p,q in v.items():
                if p =='batsman' and q =='BB McCullum':
                    for w,r in v['runs'].items():
                        if w =='batsman':
                            run+=r


    return(run)




