import re

def check_tree(tree):
  """
  Take a tree, add missing 'shape' attributes check that the correct
  figures are present

  @return: A modified tree
  """
  assert sorted(tree) == [1,2,3,4,5,'A','B','C']
  return {k: check_figure(v) for k, v in tree.items()}

def check_figure(figure):
  """
  Part of check tree, checking the figure parts. Return the modified
  figure.
  """
  return [(k, check_subfigure(v, k, figure.keys())) for k, v in figure.items()]

def check_subfigure(subfigure, id, ids):
  if subfigure == None:
    subfigure = {}
  if "shape" not in subfigure:
    subfigure["shape"] = id
  return subfigure
