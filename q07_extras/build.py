from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
def extras_runs(data=data):
    first_deliveries  = data['innings'][0]['1st innings']['deliveries']
    first_extras =0 
    sec_extras = 0
    sec_deliveries = data['innings'][1]['2nd innings']['deliveries']

    for delivery in first_deliveries:
        delivery_t = list(delivery.values())
        for k,v in delivery_t[0].items():
            if 'extras' in k:
                for k1,v1 in delivery_t[0]['extras'].items():
                    if 'wides' in k1 :
                        first_extras = first_extras + delivery_t[0]['runs']['extras']
                    if 'legbyes' in k1 :
                        first_extras = first_extras + delivery_t[0]['runs']['extras']

    for delivery in sec_deliveries:
        delivery_t = list(delivery.values())
        for k,v in delivery_t[0].items():
            if 'extras' in k:
                for k1,v1 in delivery_t[0]['extras'].items():
                    if 'wides' in k1 :
                        sec_extras = sec_extras + delivery_t[0]['runs']['extras']
                    if 'legbyes' in k1 :
                        sec_extras = sec_extras + delivery_t[0]['runs']['extras']

    difference = sec_extras - first_extras
    return difference

extras_runs(data)


