from collections import deque
from typing import List


# https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        sorted_list = []

        if numCourses <= 0:
            return False

        # a. Initialization
        graph = {i: [] for i in range(numCourses)}  # adjacency list graph
        in_degree = {i: 0 for i in range(numCourses)}  # count of incoming edges

        # b. Build the graph
        for prerequisite in prerequisites:
            parent, child = prerequisite[0], prerequisite[1]
            graph[parent].append(child)  # put the child into it's parent's list
            in_degree[child] += 1

        # c. Find all sources
        sources = deque()
        for key in in_degree:
            if in_degree[key] == 0:
                sources.append(key)

        # d. Sort
        while sources:
            vertex = sources.popleft()
            sorted_list.append(vertex)
            for child in graph[vertex]:  # get the node's children to decrement their in-degrees
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    sources.append(child)

        # if sorted_list does not contain all the courses, there is a cyclic dependency between courses
        # scheduling is not possible if there is a cyclic dependency
        return len(sorted_list) == numCourses
