# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
#     deliveries = list(data['innings'][0]['1st innings']['deliveries'])
    firstInningsExtraRuns = list()
    secondtInningsExtraRuns = list()
    
    for innings in data['innings']:
        for inning in innings:
            for delivery in innings[inning]['deliveries']:
                for deliv in delivery:
                    if '1st innings' in inning and delivery[deliv]['runs']['extras'] != 0:
                        firstInningsExtraRuns.append(delivery[deliv]['runs']['extras'])
                    if '2nd innings' in inning  and delivery[deliv]['runs']['extras'] != 0:
                        secondtInningsExtraRuns.append(delivery[deliv]['runs']['extras'])


    if secondtInningsExtraRuns > firstInningsExtraRuns :
        difference =len(secondtInningsExtraRuns) - len(firstInningsExtraRuns)
    else: difference =len(firstInningsExtraRuns) - len(secondtInningsExtraRuns) 
    
    
    return difference


