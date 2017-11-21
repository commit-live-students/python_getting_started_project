# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):

    # Your code here

   dc = data['innings'][0]['1st innings']['deliveries']

   count = 0

   for i in range(0,len(dc) - 1):
     for x in dc[i].values():
         if dc[i].values()[0]["batsman"] == "RT Ponting":
             count = count + 1

   return count
