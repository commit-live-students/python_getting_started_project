# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    first_inningextra = []
    second_inningextra = []
    # Write your code here
    first_deliveries=data['innings'][0]['1st innings']['deliveries']
    for first_delivery in first_deliveries:
        for f_delivery_no,f_delivery_info in first_delivery.items():
            try:
                #print(list(f_delivery_info['extras'].values()))
                for val in f_delivery_info['extras'].values():
                    first_inningextra.append(val)
                #first_inningextra.append(list(f_delivery_info['extras'].values()))

            except Exception:
                pass

    second_deliveries=data['innings'][1]['2nd innings']['deliveries']
    for second_delivery in second_deliveries:
        for s_delivery_no,s_delivery_info in second_delivery.items():
            try:
                for val in s_delivery_info['extras'].values():
                    second_inningextra.append(val)
                #second_inningextra.append(list(s_delivery_info['extras'].values()))
            except Exception:
                pass



    difference =(len(second_inningextra))-(len(first_inningextra))


    return difference
