% Arash Rouhani
% Project 1 in Knowledge Based AI
%

## Terminology

I'm given 3 *images*, each containing 8 *figures*, and a figure usually
contains 1-3 *subfigures*, like a circle or a rectangle. Each subfigure
contains *properties* with assigned *values*. It should be clear in my
what are properties and values in my representation.

A *figure comparison* compares two figures like A and B, but a
*comparison comparison* compares two figure comparisons.

## Format of representations

The properties of the figures are only described from the subfigures
perspective, there is is no list of properties like "the circle is left
of the triangle", rather, every property is owned by one of the
subfigures, so the circle would have a property like `position=left`.
The properties are not relative to other subfigures, hence my solution
should qualify for the extra 10% bonus.

### Technical details of the representation

I use the human readable `.yaml` format since that gets parsed to a
python value using standard libraries. `.yaml` is inherently
hierarchical and I've taken that to my advantage. Furthermore I try to
follow the DRY principles in my representation, so if the shape-property
of a subfigure is not set, then it is automatically set to the id of a
subfigure.

## Algorithm

Unfortunately I feel like I couldn't apply any of the representations
we've learned in class, they probably would've been more powerful than
my own made up one. Nevertheless, I'll briefly explain how my algorithm
works.

A step-by-step view on my algorithm can look like this:

  1. `diff_AB = compare_figures(A, B)`
  2. `diff_Cx = compare_figures(C, x)` (we loop through `x = 1..5`)
  3. `res_x = compare_diffs(diff_AB, diff_Cx)`
  4. `ans = x` where `res_x` is minimal

Here `compare_figures` takes two figures and returns a figure comparison
of the two figures. In my implementation, a figure comparison is a list
of all the ways to match up the different subfigures of the two figures,
to capture all combinations can be done in `n!` ways, where `n` is the
number of subfigures, for simplicity we assume all figures have the same
number of subfigures, if that would not be the case, we just fill up
with "dead" subfigures.

Next we compare our comparisons, or our diffs. `compare_diffs` takes two
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
the other figure comparison (say C to 4). My algorithm tries everything,
so it should never miss a correct solution, as long as it can compare
the values of the subfigures properties in a good way. However, my
program doesn't look for patterns between subfigures, so something has
to be done later for Project 2 figure 2.

So if we compare AB to C4, we look at the before-after values of AB and
see if we can match up them with before-after values of C4. If a circle
turned to a rectangle from A to B, we have a before-after value of
`circle-becomes-rectangle` in our AB comparison. When we do a
comparison comparison between AB and C4, a matching before-after value
is looked after in C4.

## Experiments

I also did some simple experiments, one for performance and one for
subtractive capability.

### Performance on my machine

I ran a test where n=4 and it took 14 seconds on my regular laptop.
Please see `reps/performence.txt` for the representation used.

Each of the provided examples run under one second.

### Subtractive capability

I added a representation which have a subfigure whose numerical value
for a property increases.  My program understands this special case,
since I've defined the difference between two values as subtraction if
it is supported. Like for instance when the `rotation`-property goes
from value `120` to value `140` from A to B, it uses subtraction to
realize that you rotate by 20 degrees.  See
`reps/subtraction-test.txt`

## Installation and running the program

    python ArashRouhani_Project_1.py

Works for me. In the unlikely case that you don't have pyyaml, I've
included the lib in the zip. If that is not working because you have
python 3, you can download the source [here] and replace the `yaml`
folder with the one in the **source** (either `.zip` or `.tar.gz`)
archive from the `lib3` folder.

[here]: http://pypi.python.org/pypi/PyYAML
