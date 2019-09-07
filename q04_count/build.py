# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
import pandas as pd
# Your Solution Here
def deliveries_count(data=data):

    # Your code here
    innings = data['innings'][0]
    firstinning = innings['1st innings']
    deliveries = firstinning['deliveries']
    df = pd.concat([pd.DataFrame(l) for l in deliveries], axis = 1).T

    runs = pd.Series.to_dict(df['runs'])
    indx = pd.DataFrame.from_dict(runs,orient = 'index')
    indx = indx.rename(columns = {'batsman':'st_batsman', 'extras':'runs_extras'})
    f_df = pd.concat([df,indx],axis=1)
    count = f_df [f_df['batsman'] == 'RT Ponting']['st_batsman'].count()

    return count
