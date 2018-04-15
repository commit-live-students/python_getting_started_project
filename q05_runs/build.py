# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    runs=0
    # Write your code here

    main_data=[]
    slices=(data['innings'][0]['1st innings']['deliveries'])
    x=0
    for a in slices:
        for b in a:
            main_data.append(slices[x][b])
            x+=1
    for a in main_data:
        if a['batsman']=='BB McCullum':
            runs+=a['runs']['batsman']
    return(runs)

#rint(BC_runs(data))
