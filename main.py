import yaml
import os.path
from src.parser import parse
from src.solver import solve

for x in range(1,5):
  file_path = "%s.yaml" % x
  if os.path.exists(file_path):
    tree = parse(file_path)
    ans = solve(tree)
    print "Solution to problem %s is %s" % (x, ans)
