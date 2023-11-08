from collections import deque
from typing import List


# Time:  O(m + n) where m is the number of edges and n is the number of courses
# Space: O(m + n)
class Solution:
    def canFinish(self, numCourses, prerequisites):
        numPrerequisites = [0] * numCourses
        nextCourses = [[] for _ in range(numCourses)]
        for nextCourse, prerequisite in prerequisites:
            numPrerequisites[nextCourse] += 1
            nextCourses[prerequisite].append(nextCourse)

        queue = deque(i for i in range(numCourses) if not numPrerequisites[i])
        while queue:
            course = queue.popleft()
            numCourses -= 1
            for nextCourse in nextCourses[course]:
                numPrerequisites[nextCourse] -= 1
                if not numPrerequisites[nextCourse]:
                    queue.append(nextCourse)

        return not numCourses


# Time:  O(m + n) where m is the number of edges and n is the number of courses
# Space: O(m + n)
class Solution:
    def dfs(self, course, courses, visit, stack):
        if stack[course]:
            return True
        if visit[course]:
            return False
        visit[course] = True
        stack[course] = True
        for nextCourse in courses[course]:
            if self.dfs(nextCourse, courses, visit, stack):
                return True
        stack[course] = False
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [[] for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            courses[prerequisite].append(course)

        visit = [False] * numCourses
        stack = [False] * numCourses
        for i in range(numCourses):
            if self.dfs(i, courses, visit, stack):
                return False
        return True

