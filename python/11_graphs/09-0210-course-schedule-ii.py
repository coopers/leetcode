from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseToPrereqs = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            courseToPrereqs[course].append(prereq)

        output = []
        complete = [False] * numCourses
        current = [False] * numCourses

        def dfs(course):
            if current[course]:
                return False
            if complete[course]:
                return True

            current[course] = True
            for prereq in courseToPrereqs[course]:
                if dfs(prereq) == False:
                    return False
                
            current[course] = False
            complete[course] = True
            output.append(course)
            return True

        if not all(dfs(course) for course in range(numCourses)):
            return []

        return output
