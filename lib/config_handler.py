import yaml

with open('/Users/kamlesh/WorkSpace/TVH/lib/config_development.yaml', 'r') as f:
    doc = yaml.load(f)

def handler(tree,node):
    return doc[tree][node]

