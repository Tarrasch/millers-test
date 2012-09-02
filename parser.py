import yaml
from src.check import check_tree
from src.image_comparing import compare_images, aux_compare_image
from src.comparision_comparing import *

stream = open("1.yaml", 'r')
tree = yaml.load(stream)

checked_tree = check_tree(tree)
# print checked_tree

go = lambda a, b: aux_compare_image(checked_tree[a], checked_tree[b], [0])
cmpAB = go("A", "B")
cmpC1 = go("C", 1)
cmpC2 = go("C", 2)
cmpC3 = go("C", 3)
print cmpAB
print cmpC1
print cmpC2
print cmpC3

print aux_compare_comparision(cmpAB, cmpC1, [0])
print aux_compare_comparision(cmpAB, cmpC2, [0])
print aux_compare_comparision(cmpAB, cmpC3, [0])

# print list(compare_images(checked_tree["A"], checked_tree["B"]))
