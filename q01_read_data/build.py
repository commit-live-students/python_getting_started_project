def read_data():
    import yaml
    with open('ipl_match.yaml', 'r') as f:
        doc = yaml.load(f)
        return doc




