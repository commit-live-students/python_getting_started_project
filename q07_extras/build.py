# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    import numpy as np
    import pandas as pd
    data1 = data['innings'][0]
    inn1 = data1['1st innings']
    deliveries_01 = inn1['deliveries']
    Trans_01 = pd.concat([pd.DataFrame(l) for l in deliveries_01],axis=1).T
    STd_01 = pd.Series.to_dict(Trans_01['runs'])
    dTD_01 = pd.DataFrame.from_dict(STd_01,orient = 'index')
    RenameCol_01 = dTD_01.rename(columns = {'batsman':'st_batsman','extras':'runs_extras'})
    con_01 = pd.concat([Trans_01, RenameCol_01], axis=1)
    extras1 = con_01[con_01['runs_extras'] > 0]['runs_extras'].count()
    extras1 = int(extras1)
    data2 = data['innings'][1]
    inn2 = data2['2nd innings']
    deliveries_02 = inn2['deliveries']
    Trans_02 = pd.concat([pd.DataFrame(l) for l in deliveries_02],axis=1).T
    STd_02 = pd.Series.to_dict(Trans_02['runs'])
    dTD_02 = pd.DataFrame.from_dict(STd_02,orient = 'index')
    RenameCol_02 = dTD_02.rename(columns = {'batsman':'st_batsman','extras':'runs_extras'})
    con_02 = pd.concat([Trans_02, RenameCol_02], axis=1)
    extras2 = con_02[con_02['runs_extras'] > 0]['runs_extras'].count()
    extras2 = int(extras2)
    difference = extras2 - extras1
    difference = int(difference)

    return difference
