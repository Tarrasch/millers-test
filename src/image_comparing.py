import operator
from copy import deepcopy
from itertools import *

def compare_images(img1, img2):
  """
  Compare two images, returning *all* ways to assign
  """
  img1 = deepcopy(img1)
  img2 = deepcopy(img2)
  while(len(img1) < len(img2)):
    insert_dead(img1, len(img1))
  while(len(img2) < len(img1)):
    insert_dead(img2, len(img2))
  return imap(aux_compare_image, repeat(img1), permutations(img2))

def insert_dead(img, id_helper):
  img += [("dead_" + str(id_helper), { "shape": "dead" })]

def aux_compare_image(img1, img2):
  """
  Compare two same-sized images, knowing the subfigure associations.

  Knowing means that we assume the 1-to-1, 2-to-2 relationship
  """
  return [
    {
      prop:
        (resolve(a, prop), resolve(b, prop))
    for prop in set(a[1].keys() + b[1].keys())}
  for a, b in izip(img1,img2)]

def resolve(subfig, prop):
  return subfig[1].get(prop)
