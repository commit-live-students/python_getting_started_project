def read_data():
    import os, yaml

    #os.chdir('/home/notebooks/data')
    #os.getcwd()

    with open ('./data/ipl_match.yaml') as yamlfile:
        yaml_data = yaml.load(yamlfile)
    return yaml_data

type(read_data())
read_data()
cliv

