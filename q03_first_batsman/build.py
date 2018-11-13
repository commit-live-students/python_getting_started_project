
# # Default Imports
# from greyatomlib.python_getting_started.q01_read_data.build import read_data
# data = read_data()

# # Your Solution
# def first_batsman(data=data):
#     name = data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']
#     return name

import pandas as pd
labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)

print(pd.Series(my_data))
print('==================')
print(pd.Series(my_data,index=labels))


