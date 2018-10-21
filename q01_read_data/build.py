
import yaml
def read_data() :
    with open('data/ipl_match.yaml','r') as fileStram:
     dictValues={}
     try :
             dictValues=yaml.load(fileStram)
     except yaml.YAMLError as fileError:
             print(fileError)
     return dictValues
print(read_data())


