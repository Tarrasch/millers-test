import operator
from copy import deepcopy
from itertools import *

def compare_figures(fig1, fig2):
  """
  Compare two figures, returning *all* ways to assign
  """
  fig1 = deepcopy(fig1)
  fig2 = deepcopy(fig2)
  while(len(fig1) < len(fig2)):
    insert_dead(fig1, len(fig1))
  while(len(fig2) < len(fig1)):
    insert_dead(fig2, len(fig2))
  return imap(aux_compare_figure, repeat(fig1), permutations(fig2))

def insert_dead(fig, id_helper):
  fig += [("dead_" + str(id_helper), { "shape": "dead" })]

def aux_compare_figure(fig1, fig2):
  """
  Compare two same-sized figures, knowing the subfigure associations.

  Knowing means that we assume the 1-to-1, 2-to-2 relationship
  """
  return [
    dict(
      (prop,
        (resolve(a, prop), resolve(b, prop)))
    for prop in set(a[1].keys() + b[1].keys()))
  for a, b in izip(fig1,fig2)]

def resolve(subfig, prop):
  return subfig[1].get(prop)
