import yaml as ym
import os as sys

def read_data():
    fName='data/ipl_match.yaml'
    dict = ym.load(open(fName))
    return dict


print('current dir : ' , sys.getcwd())
#fName='data/ipl_match.yaml'
dict_ipl=read_data()
dict_ipl['info']





