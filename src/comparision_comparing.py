from copy import deepcopy
from itertools import *

def compare_comparisions(cmp1, cmp2):
  """
  Compare two comparisions, that is, compare two comparisions of two images
  """
  cmp1 = deepcopy(cmp1)
  cmp2 = deepcopy(cmp2)
  n = max(len(cmp1), len(cmp2))
  while(len(cmp1) < len(cmp2)):
    cmp1 += [[]]
  while(len(cmp2) < len(cmp1)):
    cmp2 += [[]]
  return imap(aux_compare_comparision, repeat(cmp1), repeat(cmp2), permutations(range(n)))

def aux_compare_comparision(cmp1, cmp2, ixs):
  return sum ([
    sum ([
      delta(*cmp1[i][prop]) != delta(*cmp2[j][prop])
    for prop in set(cmp1[i].keys()) & set(cmp2[j].keys())]) +
      len(set(cmp1[i].keys()) ^ set(cmp2[j].keys()))
  for i, j in enumerate(ixs)])

def delta(a, b):
  return "unchanged" if a == b else "%s-went-%s" % (a, b)
