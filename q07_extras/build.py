

#Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
# Your Solution Here
def extras_runs (data=data):
    # Initialize the variable
    extras1 = 0
    extras2 = 0
    difference = 0
     # Read list value for deliveries
    for num in range (2):
        wides =0
        legbyes =0
        others = 0
        if (num ==0):
            inning_sequence = '1st innings'
            
        else:
            inning_sequence = '2nd innings'
        
        deliveries_info = data['innings'][num][inning_sequence]['deliveries']
        
        #iterate through deliveries
        for i in range (len(deliveries_info)):
            for key, value in (data['innings'][num][inning_sequence]['deliveries'][i]).items():
                if ('extras' in data['innings'][num][inning_sequence]['deliveries'][i][key].keys()):
                    extra_key_value = value['extras']
                    for key, value in extra_key_value.items():
                        
                        if (key == 'wides'):
                            wides += value
                        else:
                            if (key == 'legbyes'):
                                legbyes += value
                            else:
                                others +=others
        if (num ==0):
            extras1 = wides + legbyes + others
        else:
            extras2 = wides + legbyes + others
   
    if (extras1>extras2):
        difference = extras1 - extras2
    else:
        difference = extras2 - extras1
    return difference
 
extras_runs(data)




