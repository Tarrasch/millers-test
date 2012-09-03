import operator
from itertools import *
from src.image_comparing import *
from src.comparision_comparing import *

def solve(tree):
  def cmp_img(a, b):
    return compare_images(tree[a], tree[b])
  cmpABs = list(cmp_img("A", "B"))
  candidatess = list(imap(cmp_img, repeat("C"), range(1,6)))
  return choose_best_comparision(cmpABs, candidatess)

def choose_best_comparision(cmpABs, candidatess):
  ccs = imap(product_search_cmps, repeat(cmpABs), candidatess)
  return list(enumerate(ccs, start=1))

def product_search_cmps(cmps1, cmps2):
  return min(imap(compare_comparisions, *izip(*product(cmps1, cmps2))))

