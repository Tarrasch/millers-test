import yaml
from pprint import pprint
from src.checker import check_tree
from src.image_comparing import compare_images, aux_compare_image
from src.comparision_comparing import *
from src.solver import *

stream = open("3.yaml", 'r')
tree = yaml.load(stream)

ctree = check_tree(tree)
# print ctree

go = lambda a, b: next(go2(a, b))
go2 = lambda a, b: compare_images(ctree[a], ctree[b])
cmpAB = go("A", "B")

cmpC1 = go("C", 1)
cmpC2 = go("C", 2)
cmpC3 = go("C", 3)
# pprint(cmpAB)
# print cmpC1
# pprint(cmpC2)
# print cmpC3

# print aux_compare_comparision(cmpAB, cmpC1, [0])
# print aux_compare_comparision(cmpAB, cmpC1, [0])
# print aux_compare_comparision(cmpAB, cmpC2, [0])
# print aux_compare_comparision(cmpAB, cmpC3, [0])

# print compare_comparisions(cmpAB, cmpC1)

pprint (solve(ctree))

# print list(compare_images(ctree["A"], ctree["B"]))
