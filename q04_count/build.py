from greyatomlib.python_getting_started.q01_read_data.build import read_data
data1 = read_data()

# solution

#lst = []
def deliveries_count(data):
    lst = data['innings'][0]['1st innings']['deliveries']
      #print balls[0]['batsman']
    count = 0
    for d in lst:
        balls = d.values()
        if balls[0]['batsman'] == 'RT Ponting':
            count+=1
    return count

deliveries_count(data1)
