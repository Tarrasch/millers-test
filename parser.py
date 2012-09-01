import yaml
from src.check import check_tree

stream = open("2.yaml", 'r')
tree = yaml.load(stream)
print tree

checked_tree = check_tree(tree)
print checked_tree
