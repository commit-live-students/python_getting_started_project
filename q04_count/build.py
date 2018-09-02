# %load q04_count/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution Here
def deliveries_count(data=data):
    
    # Your code here
    count = 0
    
    l=data['innings'][0]['1st innings']['deliveries']
    for x in l:
        for y in x:
            if(x[y]['batsman'])=='RT Ponting':
                count=count+1
    
    
    return count

s=0
for x in range(0,120):
    z=0
    
    while z<9:
        y=z/10
        y=y+z

        try:
            #print('try')
            name = data['innings'][0]['1st innings'] ['deliveries'] [x][y] ['batsman']
            #print(name)
            #print('try')

        except Exception as e:
           # print(name)
           # s=s+1
           # print(s)
            x=x
        z=z+1
        if name=='RT Ponting':
            s=s+1
            print(s)
            
            
        #z=z+1
    #print(z)
            
name = data['innings'][0]['1st innings'] ['deliveries'] [0][0.1] ['batsman']
print(name)
if name!= 'RT Ponting':
    print('no')
name = data['innings'][0]['1st innings'] ['deliveries'] [-32]#[0.1] ['batsman']
print (name)
(data['innings'][0]['1st innings'] ['deliveries'][7])


    


print(data['innings'][0]['1st innings'] ['deliveries'] [5][0.6] ['batsman']
)
n = data['innings'][0]['1st innings'] ['deliveries']
total=len(n)
print(total)
for x in range(0,total): 
    print((x))


n = data['innings'][0]['1st innings'] ['deliveries']
total=len(n)
print(total)
for x in range(0,total):
    y=x+1
    y=y/10
    z=0.7
    
        name = data['innings'][0]['1st innings'] ['deliveries'] [x][y] ['batsman']

        print(name)
n = data['innings'][0]['1st innings'] ['deliveries']
total=len(n)
print(total)
for x in range(0,7):
    
    y=x+1
    y=y/10
   # if y > 0.6:
    #    y=y-0.1
    #    y=y+1
    name = data['innings'][0]['1st innings'] ['deliveries'] [x][y] ['batsman']
    print(name)
count=0
for x in range(0,120):
    y=0.1
    while y<0.8:
        z=y
        #z=z+x
        try:    
            xyz=data['innings'][0]['1st innings']['deliveries'][x][0.1].get('batsman')
        except Exception:
            z=z
            #print(x)
        else:
            #print(xyz)
            #print(y)
            print(y)
        y=y+0.1
type(data['innings'][0]['1st innings']['deliveries'])
l=data['innings'][0]['1st innings']['deliveries']
len(data['innings'][0]['1st innings']['deliveries'])
l2=[item for item in l if item=='RT Ponting']

typ(l[0])
for x in l:
    for y in x:
        print(x[y]['batsman'])
            
        
c=0
for x in l:
    for y in x:
        if(x[y]['batsman'])=='RT Ponting':
            c=c+1
            print(c)
c=0
for x in l:
    for y in x:
        if(x[y]['batsman'])=='RT Ponting':
            c=c+1
print(c)


