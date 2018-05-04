from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
def BC_runs(data):
    ponting_list=[]
    runs=0
    deliveries = data['innings'][0]['1st innings']['deliveries']
    for delivery in deliveries:
        delivery_t = list(delivery.values())
        if delivery_t[0]['batsman']=='BB McCullum':
            ponting_list.append(delivery_t[0])
    for ball_face in ponting_list:
        run = int(ball_face['runs']['batsman'])
        runs =  runs+run
    return(runs)
BC_runs(data)


