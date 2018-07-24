# # %load q07_extras/build.py



# v_data.build import read_ipl_data_csv
# import numpy as np
# from greyatomlib.python_getting_started.q01_read_data.build import read_data
# data = read_data()
# # path = 'data/ipl_matches_small.csv'
# # Enter Code Here
# def get_total_extras():
#     data = read_data()
#     data = read_ipl_data_csv(data,'int64')
#     extras = data[:,17]
#     return int(np.sum(extras))
               
# print(get_total_extras())




from greyatomlib.python_getting_started.q01_read_data.build import read_data

data = read_data()
# Your Solution
def extras_runs(data=data):
    extras_1=[]
    extras_2=[]
    deliveries=data['innings'][0]['1st innings']['deliveries']
    for delivery in deliveries:
        for key in delivery:
            extras_1.append(delivery[key]['runs']['extras'])
    deliveries=data['innings'][1]['2nd innings']['deliveries']
    for delivery in deliveries:
        for key in delivery:
            extras_2.append(delivery[key]['runs']['extras'])
    count1=0
    count2=0
    for extra in extras_1:
        if extra>0:
            count1+=1
    for extra in extras_2:
        if extra>0:
            count2+=1
    difference=count2-count1
    return difference


extras_runs()


