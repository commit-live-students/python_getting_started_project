# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
def BC_runs(data):
    find1=data['innings']
    find2=find1[0]
    find3=find2['1st innings']['deliveries']
    runs = 0
    for i in find3:
        if i.values()[0]['batsman']=='BB McCullum':
            runs=runs+i.values()[0]['runs'].values()[0]
    return(runs)
