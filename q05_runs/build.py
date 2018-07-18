# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    import numpy as np
    import pandas as pd
    data1 = data['innings'][0]
    data2 = data1['1st innings']
    data3 = data2['deliveries']
    data4 = pd.concat([pd.DataFrame(l) for l in data3],axis=1).T
    data5 = pd.Series.to_dict(data4['runs'])
    data6 = pd.DataFrame.from_dict(data5,orient = 'index')
    data6 = data6.rename(columns = {'batsman':'st_batsman','extras':'runs_extras'})
    data7 = pd.concat([data4, data6], axis=1)
    runs = data7[data7['batsman'] == 'BB McCullum']['st_batsman'].sum()
    runs = int(runs)
    
    return (runs)
