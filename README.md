* Linear data structure (linked list, array, or string)?
    * Explicitely sorted?
        * Find a certain element?
            * **Binary search**
        * Given **K** sorted arrays perform a *sorted traversal* of *all* the elements of *all* arrays?
            * **K-way Merge **(Use of (multiple) heap(s), like MinHeap and/or Max Heap / Prioroty Queue)
        * There is a *target*value to match?
            * **Two Pointers (probably with opposite directions)**
        * Duplicates to be *removed*?
            * **Two Pointers (probably with opposite directions)**
    * Unsorted or it does not matter?
        * Intersection?
            * **Two Pointers**
        * Values in a given range?
            * Find a missing/duplicate/smallest number among nums (in given range)?
                * **Cyclic sort**
        * Smallest/largest/median elements of a stream?
            * **Two heaps**
        * Contains a set of pair elements, or a triplet or even a subarray?
            * **Two Pointers (probably with opposite directions)**
        * Modify IN-PLACE?
            * **Two Pointers (probably with opposite directions)**
        * Top/smallest/frequent ‘K’ elements of a given set?
            * **Top K elements**
        * Find the longest/shortest substring, subarray?
            * **Sliding window**
        * Find contiguous *longest*, *shortest*, *average* or *target* value?
            * **Sliding window**
        * Is it a linked list?
            * Reverse IN-PLACE?
                * **In-place reversal of linked list**
            * Find loop?
                * **Fast and Slow Pointers (same direction)**
            * Find the position of a certain element or the overall length of the linked list?
                * **Fast and Slow Pointers (same direction)**
        * Deals with with *intervals*, *overlapping items* or *merging intervals*.?
            * **Merge intervals**
* Is it a  graph?
    * No cycles?
        * Traverse a tree in a level-by-level fashion (or level order traversal)?
            * **BFS**
        * Traverse a tree with in-order, preorder, or postorder?
            * **DFS**
        * Searching for something where the node is closer to a leaf?
            * **DFS**
    * Scheduling or grouping problem which has dependencies between items?
        * **Topological sort**
* Is it a set / sets?
    * Values in a given range?
        * Find a missing/duplicate/smallest number among nums (in given range)?
            * **Cyclic sort**
    * Smallest/largest/median elements of a set?
        * **Two heaps**
    * Combinations or permutations of a given set?
        * **Subsets**
    * Top/smallest/frequent ‘K’ elements of a given set?
        * **Top K elements**
    * Priority Queue, Scheduling?
        * **Two Heaps**


# Data Structures and Algorithms

Implementation of different algorithms and data structures with Golang.

1. [Sorting](ds_and_algos/sorting)
1. [Stacks and Queues](ds_and_algos/stack_queue)
1. [Heap](ds_and_algos/heap)
1. [Linked List](ds_and_algos/linked_list)
1. [Binary Tree](ds_and_algos/binary_tree)
1. [Binary Search Tree](ds_and_algos/binary_search_tree)
1. [Functional Programming](go_standard_lib/functional)
1. [Golang Built In Functionality](go_standard_lib)
1. [Testing](go_standard_lib/testing)
1. [Selected Problems](./misc)

