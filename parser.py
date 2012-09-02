import yaml
from src.check import check_tree
from src.image_comparing import compare_images, aux_compare_image

stream = open("1.yaml", 'r')
tree = yaml.load(stream)

checked_tree = check_tree(tree)
# print checked_tree

print list(compare_images(checked_tree["A"], checked_tree["B"]))
