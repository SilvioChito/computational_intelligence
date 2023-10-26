# Assignment n.1 - Set Covering

## Introduction to the problem  

The following code is my proposal to the set covering problem, in which we aim to cover a certain number of items whith the least number of sets of items.

The solution exploits the A* search, in order to collect the minimum number of sets that cover all the items.

## Solving steps

The algorithm tries to get an optimistic estimate of how many sets will be needed, starting from a specific state, which is represented in terms of 2 sets: the taken ones and the not taken ones.

Firstly I decided to create a structure that could tell me how many sets manage to cover different number of items.
By knowing the set of not taken sets so far for a certain state, I can in this way optimize how I could take the remaining items starting from the largest possible set of elements (which is stored in the previous mentioned structure). Therefore, we always try to take the set that optimistically covers most of the elements. If a single set cannot cover all the remaining elements, I take a second (smaller) one that manages to do that and so on...

## Implementation

The sets represent how many (and which) items are taken and which aren't, and are represented in terms of tuples of boolean values.
Instead, I used a dictionary for the structure that contains the mapping between the number of elements contained into a set and the number of sets that actually contain that specific number of items.
This dictionary is initialized only at the beginning, and whenever I use my heuristic function, it copies and updates it with the sets that have been already taken.


Code developed jointly with [MichelangeloCaretto](https://github.com/rasenqt/computational_intelligence23_24) 