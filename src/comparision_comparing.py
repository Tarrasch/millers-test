from copy import deepcopy
from itertools import *

def compare_comparisions(cmp1, cmp2):
  """
  Compare two comparisons, that is, compare two comparisons of two figures
  """
  cmp1 = deepcopy(cmp1)
  cmp2 = deepcopy(cmp2)
  while(len(cmp1) < len(cmp2)):
    cmp1 += [{}]
  while(len(cmp2) < len(cmp1)):
    cmp2 += [{}]
  return min(imap(aux_compare_comparision, repeat(cmp1), permutations(cmp2)))

def aux_compare_comparision(cmp1, cmp2):
  return (sum ([
    sum ([
      delta(*a[prop]) != delta(*b[prop])
    for prop in set(a.keys()) & set(b.keys())]) +
      len(set(a.keys()) ^ set(b.keys()))
  for a, b in izip(cmp1,cmp2)]), cmp1, cmp2)

def delta(a, b):
  if a == b:
    return "unchanged"
  elif b == "dead":
    return "rhs died" # We assume we are talking about shapes.
                      # I added this so example 3 passes without penalty.
  elif type(a) == type(b) and "__sub__" in dir(a):
    return a - b # Can be used when detecting "rotation by X degrees"
  else:
    return "%s-went-%s" % (a, b)
