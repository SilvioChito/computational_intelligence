# HALLOWEEN Challenge
The following is a proposal for the [Halloween challenge](https://github.com/squillero/computational-intelligence/blob/master/2023-24/Halloween.ipynb) of the Computation Intelligence class. 


## Iterated Local Search for set covering problem

My solution for the Halloween challenge is made by means of iterated local search. In particular, the algorithm looks for a local optimum and when it finds it, it "perturbs" its state looking for a new possible local optimum in the nearby.
The search is done until the current local optimum (our "home") has a lower cost with respect to the new predicted state, or in case the time is out (200 iteration reached).

The following are the results for the combination of parameters given by the challenge:

| **Number of points** | Density | Calls to the fitness function | Optimal cost
| --- | --- | --- | --- |
| 100 | 0.3 | 132 | (100, -10) |
| 100 | 0.7 | 116 | (100, -4) |
| 1000 | 0.3 | 148 |(1000, -18) |
| 1000 | 0.7 | 122 | (1000, -7) |
| 5000 | 0.3 | 148 | (5000, -20) |
| 5000 | 0.7 | 126 | (5000, -9) |