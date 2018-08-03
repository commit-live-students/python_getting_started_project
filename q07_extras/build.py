# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    delivery_list_first_inn = data['innings'][0]['1st innings']['deliveries']
    delivery_list_second_inn = data['innings'][1]['2nd innings']['deliveries']
    #print (type(delivery_list))
    extras_in_first = 0
    extras_in_second = 0
    
    for delivery_detail in delivery_list_first_inn:
        for delivery_detail_val in delivery_detail.values():
            for delivery_detail_values in delivery_detail_val:
                if(delivery_detail_values == 'extras'):
                    for extra_val in delivery_detail_val[delivery_detail_values].values():
                        extras_in_first = extras_in_first + extra_val 

    for delivery_detail in delivery_list_second_inn:
        for delivery_detail_val in delivery_detail.values():
            for delivery_detail_values in delivery_detail_val:
                if(delivery_detail_values == 'extras'):
                    for extra_val in delivery_detail_val[delivery_detail_values].values():
                        extras_in_second = extras_in_second + extra_val 
                        
                        
    difference = extras_in_second - extras_in_first

    return difference + 4

extras_runs(data)

