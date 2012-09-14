% Arash Rouhani
% Project 1 in Knowledge Based AI
%

## Terminology

I'm given 3 *images*, each containing 8 *figures*, and a figure usually
contains 1-3 *subfigures*, like a circle or a rectangle. Each subfigure
contains *properties* with assigned *values*.

A *figure comparison* compares two figures like A and B, but a
*comparison comparison* compares two figure comparisons.

## Syntax of representations

The properties of the figures are only described from the subfigures
perspective, there is no list of properties like "the circle is left of the
triangle", rather, properties are owned by the subfigures, so the circle would
instead have a property like `position=left`.  The properties are not relative
to other subfigures, hence my solution should qualify for the extra 10% bonus.

### Technical details of the representation

I use the human readable `.yaml` format since that gets parsed to a python
value using standard libraries. `.yaml` is inherently hierarchical and I've
taken that to my advantage. Furthermore I try to follow the DRY principles in
my representation, if the shape-property of a subfigure is not set, my program
automatically sets it to the id of the subfigure.

## Algorithm

A step-by-step view of my algorithm can look like this:

  1. `cmp_AB = compare_figures(A, B)`
  2. `cmp_Cx = compare_figures(C, x)` (we loop through `x = 1..5`)
  3. `res_x = compare_cmps(cmp_AB, cmp_Cx)`
  4. `ans = x` where `res_x` is minimal

Here `compare_figures` takes two figures and returns a figure comparison of the
two figures. In my implementation, a figure comparison is a list of all the
ways to match up the different subfigures of the two figures. The number of
combinations are `n!`, where `n` is the number of subfigures.  In this analysis
we assume all figures have the same number of subfigures. If that would not be
the case, the program inserts "dead" subfigures to balance it.

Next we compare our comparisons. `compare_cmps` takes two image comparisons and
scores how much they are alike. The logic of `compare_cmps` is aware that a
image comparison is in fact a list, and it analyzes the pairs in the Cartesian
product of the two lists. Both lists contain `n!` elements, so we are comparing
two comparisons n!^2^ times, also, when doing such a comparison we want to
match each subfigure-difference with every other subfigure difference, which
adds another n!, resulting in the total of n!^3^. Luckily though, the last n!
is only a extremely naive solution to the *maximum weighted bipartite matching*
problem, which is O(n^4^). But O(n^4^) is nothing compared to O(n!).  We
conclude that the time complexity could have been O(n!^2^) but my
implementation is O(n!^3^) in time.

It should be noted that the space complexity is not in the order of O(n!). The
program does not save the intermediate lists of a figure comparison in memory,
rather, everything is implemented using iterators. So in contrast to the time
complexity, the memory footprint can be seen as nonexistent.

## Justification and how it works

It should be clear from my complexity analysis that I basically try to mix and
match the figures and subfigures in all possible ways, and rank each figure
comparison (say A to B) by how good one could match it with the other figure
comparison (say C to 4). My algorithm is exhaustive, so it will also "visit"
the correct configuration, which is a necessity for always being correct.

### Comparing subfigure-comparisons

So if we compare AB to C4, we look at the *before-after* values of AB and see if
we can match them up with before-after values of C4. If a circle turned into a
rectangle from A to B, we have a before-after value of
`circle-becomes-rectangle` in our AB comparison. When we do a comparison
comparison between AB and C4, a before-after value that is similar is looked
for in C4. If no similar value is found, we add a penalty to the comparison
between AB and C4.

There is some intelligence when looking for similar before-after values.  For
example, we don't consider `circle-becomes-rectangle` similar to
`square-becomes-rectangle`. But we do consider `circle-stays-circle` similar to
`square-stays-square`. For the exact behavior of comparing these values, please
look at the actual implementation of `src.delta` in `comparison_comparing.py`.
Also, look at the subtraction experiment I've done.

### Critique of design

Some shortcomings of the program are revealed from my conducted experiments
below. Here are some other problems worth mentioning.

  * The program does not infer relations between subfigures within the same
    figure, it only compares subfigures across figures.  It's not necessary for
    this project, but it will be for project 2 image 2.
  * There is no ranking of properties, any property is as important as any
    other. But this can be resolved easily.
  * The program have no defined behavior when there are ties. This will become
    less of a problem if each property is considered diffrently important
    though.

## Experiments

I did some simple experiments, one for performance and one for subtractive
capability.

### Performance on my machine

I ran a test where `n=4` and it took 14 seconds on my laptop.
Please see `reps/performence.txt` for the representation used.

Each of the provided examples run under one second, since they have only three
figures or less. This experiment should make clear that my program is not
designed to handle more than a very few subfigures.

### Subtractive capability

I added a representation which have a subfigure whose numerical value
for a property increases.  My program understands this special case,
since I've defined the difference between two values as subtraction if
it is supported. Like for instance when the `rotation`-property goes
from value `120` to value `140` from A to B, it uses subtraction to
realize that you rotate by 20 degrees.  See
`reps/subtraction-test.txt`

## Installation and running the program

      $ python ArashRouhani_Project_1.py

Works for me. In the unlikely case that you don't have pyyaml, I've
included the lib in the zip. If that is not working because you have
python 3, you can download the source [here] and replace the `yaml`
folder with the one in the **source** (either `.zip` or `.tar.gz`)
archive from the `lib3` folder.

[here]: http://pypi.python.org/pypi/PyYAML
