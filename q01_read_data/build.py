import yaml

def read_data():
 
    with open('./data/ipl_match.yaml', 'r') as stream:
        try:
            MyDict = yaml.load(stream)
            print(yaml.load(stream))
        except yaml.YAMLError as exc:
            print(exc)
    return MyDict

read_data()
read_data()



