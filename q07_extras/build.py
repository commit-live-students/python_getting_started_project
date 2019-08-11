# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    deliveries = dict()
    # Write your code here
    first_deliveries = data['innings'][0]['1st innings']['deliveries']
    second_deliveries = data['innings'][1]['2nd innings']['deliveries']

    def deliverylooper(deliveries):
        innings_extras = []
        for i in deliveries:
                deliver = i.values()
                #print balls
                for x in deliver:
                    ball = x
                   #so far dict
                    for type in ball:
                        #print type

                        if type == 'runs':
                            innings_extras.append(ball[type]['extras'])

        innings_extras = [i for i in innings_extras if i > 0]
        extras = len(innings_extras)
        return extras

    first_innings_extra = deliverylooper(first_deliveries)

    second_innings_extra = deliverylooper(second_deliveries)

    difference = second_innings_extra-first_innings_extra


    return difference

print extras_runs()
