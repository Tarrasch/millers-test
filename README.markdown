% Arash Rouhani
% Project 1 in Knowledge Based AI
%

## Terminology

I'm given 3 *images*, each containing 8 *figures*, and a figure contains
usually 1-3 *subfigures*, like a circle or the rectangle. Each
subfigure then contains *properties* with associated *values*. It should
be clear in my what are properties and values in my representation.

An *figure comparison* can compare two figures like A and B, but a
*comparison comparison* compares to figure comparisons.

## Format of representations

Properties of the figures are only described from each subfigures
perspective, that is I have no list of properties like "circle is left
of triangle", rather, every property is owned by one of the subfigures,
so the circle would have a property like `position=left`.  The
properties are not relative to other subfigures, hence my solution
should qualify for the extra 10% bonus.

### Technical details

I use the human readable `.yaml` format since that easily gets parsed to
a python value. `.yaml` is inherently hierarchical and I've taken that
to my advantage. Furthermore I try to follow the DRY principles in my representation,
so if the shape-property of a subfigure is not set, then it is
automatically set to the id of a subfigure.

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

Here `compare_imgs` takes two figures and returns a figure comparison
of the two figures. In my implementation, a figure comparison is a list
of all the ways to match up the different subfigures of the two figures,
to capture all combinations can be done in `n!` ways,
where `n` is the number of subfigures, for simplicity we assume all
figures
have the same number of subfigures, if that would not be the case, we just
fill up with "dead" subfigures.

Next we compare our comparisons, or our diffs. `compare_diffs` take two
diffs and scores how much these diffs are relatively alike. The logic of
`compare_diffs` is aware that a diff is in fact a list, and it does
comparing between the elements in the two lists (set product), and both
the lists should contain `n!` elements, so we are comparing two
comparisons n!^2^ times, also, when doing such a comparison we want to
match each subfigure-difference with every other subfigure difference,
which also adds another n!, resulting in the total of n!^3^. Luckily
though, the last n! is only a extremely naive solution to the *maximum
weighted bipartite matching* problem, which is O(n^4^). But O(n^4^) is nothing
compared to O(n!). We conclude that the complexity could have been
O(n!^2^) but my naive implementation is O(n!^3^).

## Justification and how it works

It should be clear from my complexity analysis that I basically try to
mix and match the figures and subfigures in all possible ways, and rank
each figure comparison (say A to B) by how good one could match it with
the other figure comparison (say C to 4). My algorithm tries
everything, so it should never miss a correct solution, as long as it can
compare the values of the figures properties in a good way.

So if we compare AB to C4, we look at the before-after values of AB and
see if we can match up them with before-after values of C4. If a circle
turned to a rectangle from A to B, we have a before-after value of
`circle-becomes-rectangle` in our AB comparison. When we do a
comparison comparison between AB and C4, a matching before-after value
is looked after in C4.

## Experiments

I also did some simple experiments, one for performance and one for
intelligence.

### Performance on my physical machine

I ran a test where n=4 and it took 14 seconds. Please see
`reps/performence.txt` for the representation used.

But the provided examples from the project run all under one second.

### Intelligence

I added a test where a properties numerical value increases, indeed my
program understands that special case, like for instance when the A to B
change is that you rotate by 20 degrees. See `reps/subtraction-test.txt`
