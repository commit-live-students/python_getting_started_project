# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    import numpy as np
    import pandas as pd
    data1 = data['innings'][1]
    data2 = data1['2nd innings']
    data3 = data2['deliveries']
    data4 = pd.concat([pd.DataFrame(l) for l in data3],axis=1).T
    wicket1 = data4[data4['wicket'].notnull()]['wicket']
    wicket_STd = pd.Series.to_dict(wicket1)
    wicket_dTD = pd.DataFrame.from_dict(wicket_STd,orient = 'index')
    bowled_players =  list(wicket_dTD[wicket_dTD['kind'] == 'bowled']['player_out'])

    return bowled_players
