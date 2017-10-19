# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    deliveries_first_innings = data['innings'][0]['1st innings']['deliveries']
    deliveries_second_innings = data['innings'][1]['2nd innings']['deliveries']
    extras_first_innings = 0
    extras_second_innings = 0
    for each_delivery in deliveries_first_innings:
        for deliveryNumber, deliveryInfo in each_delivery.items():
            if (deliveryInfo['runs']['extras']) > 0:
                extras_first_innings += 1
    #print(extras_first_innings)
    for each_delivery in deliveries_second_innings:
        for deliveryNumber, deliveryInfo in each_delivery.items():
            if (deliveryInfo['runs']['extras']) > 0:
                extras_second_innings += 1
    #print(extras_second_innings)
    # Write your code here


    difference = extras_second_innings - extras_first_innings
    #print(difference)

    return difference
