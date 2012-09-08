# Project 1

## Format of representations

I use the humanreadable `.yaml` format since that easily gets parsed to
a python value. `.yaml` is inherently hierarchical and I've taken that
to my advantage.

Properties of the images are only described from each subfigures
perspective, that is I have no list of properties like "circle is left
of triangle", rather, every property is owned by one of the subfigures,
so the circle would have a property like "I'm on the left of triangle".

I use some syntactic sugar to follow the DRY principles in my
representation, see `src/checker.py` for details.

## Algorithm

Unfortunately I feel like I couldn't apply any of the representations
we've learned in class, they probably would've been more powerful than
my own made up one. Nevertheless, I'll briefly explain how my algorithm
works.

A step-by-step view on my algorithm can look like this:

  1. `diff_AB = compare_imgs(A, B)`
  2. `diff_Cx = compare_imgs(C, x)` (we loop through `x = 1..5`)
  3. `res_x = compare_diffs(diff_AB, diff_Cx)`
  4. `ans = x` where `res_x` is minimal

Here `compare_imgs` takes two images and returns a *comparision value*
of the two images. In my implemenation, a *comparision value* is a list
of all the ways to match up the diffrent subfigures of the two images,
to capture all combinations can be done in `n!` ways,
where `n` is the number of subfigures, for simplicity we assume all images
have the same number of subfigures, if that would not be the case, we just
fill up with "dead" subfigures.

Next we compare our comparisions, or our diffs. `compare_diffs` take two
diffs and scores how much these diffs are relatively alike. The logic of
`compare_diffs` is aware that a diff is in fact a list, and it does
productwise comparing between the elements in the two lists, and both
the lists should contain `n!` elements, so we are comparing two
comparisions n!^2^ times, also, when doing such a comparision we want to
match each subfigure-difference with every other subfigure difference,
which also adds another n!, resulting in the total of n!^3^. Luckily
though, the last n! is only a extremely naive solution to the *maximum
weighted bipartite matching* problem, which is O(n^4^). But O(n^4^) is nothing
compared to O(n!). We conclude that the complexity could have been
O(n!^2^) but my naive implementation is O(n!^3^).
