# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here

    extras_per_innings = [0,0]

    for innings in range(len([data][0]['innings'])):
        for inn_name, inn_details in [data][0]['innings'][innings].items():
            for attr_name, del_info in inn_details.items():
                if attr_name <> 'team':
                    for del_details in del_info:
                        for delivery, delivery_outcome in del_details.items():
                            if 'extras' in delivery_outcome:
                                extras_per_innings[innings] += 1

    difference = extras_per_innings[1] - extras_per_innings[0]


    return difference
