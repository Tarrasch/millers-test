import re

def check_tree(tree):
  """
  Take a tree, add missing 'shape' attributes, expand upon the syntactic
  suger sugar by turning C{123} to C{val: 123} and check that all figure
  values exists.

  This method also checks that the correct images are present

  @return: A modified tree
  """
  assert sorted(tree) == [1,2,3,4,5,'A','B','C']
  return {k: check_image(v) for k, v in tree.items()}

def check_image(image):
  """
  Part of check tree, checking the image parts. Return the modified
  image.
  """
  return [(k, check_subfigure(v, k, image.keys())) for k, v in image.items()]

def check_subfigure(subfigure, id, ids):
  if subfigure == None:
    subfigure = {}
  if "shape" not in subfigure:
    subfigure["shape"] = id
  return {k: check_property(v, ids) for k, v in subfigure.items()}

def check_property(prop, ids):
  if type(prop) is not list:
    prop = [ "val", prop ]
  if prop[0] == "fig":
    assert prop[1] in ids
  assert re.match(r"^(fig|val)$", prop[0])
  assert len(prop) == 2
  return prop
