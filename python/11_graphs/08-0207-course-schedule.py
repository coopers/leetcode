from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseToPrereqs = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            courseToPrereqs[course].append(prereq)

        taken = [False] * numCourses
        def dfs(course):
            if taken[course]:
                return False
            if not courseToPrereqs[course]:
                return True
            
            taken[course] = True
            for prereq in courseToPrereqs[course]:
                if not dfs(prereq):
                    return False
            
            taken[course] = False
            courseToPrereqs[course] = []
            return True

        return all(dfs(course) for course in range(numCourses))
