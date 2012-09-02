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
  return imap(aux_compare_image, repeat(img1), repeat(img2), permutations(range(n)))

def insert_dead(img, id_helper):
  subfigure = { "shape": "dead" }
  img["dead_" + str(id_helper)] = subfigure

def aux_compare_image(img1, img2, ixs):
  """
  Compare two same-sized images, knowing the subfigure associations

  @param ixs: The asociations
  """
# TODO: Implement fig-lookup
  return [ 
    {
      prop: "{0} becomes {1}".format(img1[i][1].get(prop), img2[j][1].get(prop))
    for prop in set(img1[i][1].keys() + img2[j][1].keys())}
  for i, j in enumerate(ixs)]
  
