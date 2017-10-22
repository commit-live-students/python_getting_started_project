# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

import pandas as pd
# Your Solution
def bowled_out(data=data):

    # Write your code here
    innings = data['innings'][1]
    firstinning = innings['2nd innings']
    deliveries = firstinning['deliveries']
    df = pd.concat([pd.DataFrame(l) for l in deliveries], axis = 1).T

    wicket = df[df['wicket'].notnull()]['wicket']
    wicket_s = pd.Series.to_dict(wicket)
    wicket_d = pd.DataFrame.from_dict(wicket_s, orient = 'index')
    bowled_players = list(wicket_d[wicket_d['kind']=='bowled']['player_out'])

    return bowled_players
