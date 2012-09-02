import operator
from copy import deepcopy
from itertools import *

def compare_images(img1, img2):
  """
  Compare two images, returning *all* ways to assign
  """
  img1 = deepcopy(img1)
  img2 = deepcopy(img2)
  n = max(len(img1), len(img2))
  while(len(img1) < len(img2)):
    insert_dead(img1, len(img1))
  while(len(img2) < len(img1)):
    insert_dead(img2, len(img2))
  return imap(aux_compare_image, repeat(img1), permutations(img2))

def insert_dead(img, id_helper):
  img += [("dead_" + str(id_helper), { "shape": ["val", "dead"] })]

def aux_compare_image(img1, img2):
  """
  Compare two same-sized images, knowing the subfigure associations.
 
  Knowing means that we assume the 1-to-1, 2-to-2 relationship
  """
  return [
    {
      prop:
        (resolve(img1, a, prop), resolve(img2, b, prop))
    for prop in set(a[1].keys() + b[1].keys())}
  for a, b in izip(img1,img2)]

def resolve(img, subfig, prop):
  got = subfig[1].get(prop)
  if got == None:
    return None
  elif got[0] == 'val':
    return got[1]
  else:
    img_ids = map(operator.itemgetter(0), img)
    return "fig-" + str(img_ids.index(got[1]))
