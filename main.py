import yaml
from src.parser import parse
from src.solver import solve

for x in range(1,4):
  tree = parse("%s.yaml" % x)
  ans = solve(tree)
  print "Solution to problem %s is %s" % (x, ans)
