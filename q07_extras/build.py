
#Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
# Your Solution Here
def extras_runs (data=data):
    # Initialize the variable
    bowled_players =[]
    extras1 = 0
    extras2 = 0
    wides =0
    legbyes =0
    difference = 0
     # Read list value for deliveries
    deliveries_info = data['innings'][0]['1st innings']['deliveries']
    for i in range (len(deliveries_info)):
        for key, value in (data['innings'][0]['1st innings']['deliveries'][i]).items():
            if ('extras' in data['innings'][0]['1st innings']['deliveries'][i][key].keys()):
                extra_key_value = value['extras']
                for key, value in extra_key_value.items():
                    if (key == 'wides'):
                        wides += value
                    if (key == 'legbyes'):
                        legbyes += value
                extras1 = wides + legbyes
    wides =0
    legbyes =0       
    # Read list value for deliveries
    deliveries_info = data['innings'][1]['2nd innings']['deliveries']
    for i in range (len(deliveries_info)):
        for key, value in (data['innings'][1]['2nd innings']['deliveries'][i]).items():
            if ('extras' in data['innings'][1]['2nd innings']['deliveries'][i][key].keys()):
                extra_key_value = value['extras']
                for key, value in extra_key_value.items():
                    if (key == 'wides'):
                        wides += value
                    if (key == 'legbyes'):
                        legbyes += value
                extras2 = wides + legbyes
    if (extras1>extras2):
        difference = extras1 - extras2
    else:
        difference = extras2 - extras1
    return difference
 
extras_runs(data)


