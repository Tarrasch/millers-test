import operator
from itertools import *
from src.figure_comparing import *
from src.comparision_comparing import *
import sys

def solve(tree):
  return min(solve_verbose(tree), key=operator.itemgetter(1))[0]

def solve_verbose(tree):
  def cmp_fig(a, b):
    return compare_figures(tree[a], tree[b])
  cmpABs = list(cmp_fig("A", "B"))
  candidatess = list(imap(cmp_fig, repeat("C"), range(1,6)))
  return make_comparisions(cmpABs, candidatess)

def make_comparisions(cmpABs, candidatess):
  ccs = imap(product_search_cmps, repeat(cmpABs), candidatess)
  return list(enumerate(ccs, start=1))

def product_search_cmps(cmps1, cmps2):
  dic = { 'i': 0 } # http://stackoverflow.com/a/3190783/621449
  def verbose_cc(cmp1, cmp2):
    dic['i'] = dic['i'] + 1
    sys.stdout.write('\b' * 100 + "working %s ..." % dic['i'])
    return compare_comparisions(cmp1, cmp2)
  res = min(imap(verbose_cc, *izip(*product(cmps1, cmps2))))
  sys.stdout.write('\b' * 100)
  return res

