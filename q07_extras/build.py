from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    ex_1 = data['innings'][0]['1st innings']['deliveries']
    count = 0
    count1 = 0
    extra = 0
    extra1 = 0
    ext1 = 0
    ex_2 = data['innings'][1]['2nd innings']['deliveries']
    for ext_1 in range(len(ex_1)):
        ball_1 = ex_1[count].keys()
        ext_1 = ex_1[count][ball_1[0]]['runs']['extras']
        if ext_1 >= 1:
            extra += 1
        count += 1
    #print extra
    for ext_2 in range(len(ex_2)):
        ball_2 = ex_2[count1].keys()
        ext_2 = ex_2[count1][ball_2[0]]['runs']['extras']
        if ext_2 >= 1:
            extra1 += 1

        count1 += 1
    #print extra1

    difference = extra1 - extra
    return difference
print extras_runs()
