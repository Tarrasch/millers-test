import yaml
from src.checker import check_tree

def parse(path):
  """
  Please always use to this ensure you get a checked tree

  @return A tree which has been checked
  """
  stream = open(path, 'r')
  return check_tree(yaml.load(stream))
