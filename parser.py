import yaml
from pprint import pprint
from src.checker import check_tree
from src.figure_comparing import compare_figures, aux_compare_figure
from src.comparision_comparing import *
from src.solver import *

# stream = open("1.yaml", 'r')
stream = open("subtraction-test.yaml", 'r')
# stream = open("big.yaml", 'r')
tree = yaml.load(stream)

ctree = check_tree(tree)
# print ctree

go = lambda a, b: next(go2(a, b))
go2 = lambda a, b: compare_figures(ctree[a], ctree[b])

cmpAB = go("A", "B")
cmpC1 = go("C", 1)
cmpC2 = go("C", 2)
cmpC3 = go("C", 3)
cmpC4 = go("C", 4)
cmpC5 = go("C", 5)
# pprint(cmpAB)
# print cmpC1
# pprint(cmpC2)
# print cmpC3

# print compare_comparisions(cmpAB, cmpC1)
# print compare_comparisions(cmpAB, cmpC2)
# print compare_comparisions(cmpAB, cmpC3)
# print compare_comparisions(cmpAB, cmpC4)
# print compare_comparisions(cmpAB, cmpC5)

# pprint (ctree)
# exit()
pprint (solve_verbose(ctree))
