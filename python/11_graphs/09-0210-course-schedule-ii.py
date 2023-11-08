from collections import defaultdict, deque
from typing import List


# Time:  O(m + n) where m is the number of edges and n is the number of courses
# Space: O(m + n)
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        numPrerequisites = [0] * numCourses
        courses = defaultdict(list)
        for course, prerequisite in prerequisites:
            numPrerequisites[course] += 1
            courses[prerequisite].append(course)
        
        satisfied = deque(i for i in range(numCourses) if numPrerequisites[i] == 0)
        res = []
        while satisfied:
            course = satisfied.popleft()
            res.append(course)
            for nextCourse in courses[course]:
                numPrerequisites[nextCourse] -= 1
                if numPrerequisites[nextCourse] == 0:
                    satisfied.append(nextCourse)

        return res if len(res) == numCourses else []


# Time:  O(m + n) where m is the number of edges and n is the number of courses
# Space: O(m + n)
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        numPrerequisites = [0] * numCourses
        courses = defaultdict(list)
        for course, prerequisite in prerequisites:
            numPrerequisites[course] += 1
            courses[prerequisite].append(course)
        
        res = [i for i in range(numCourses) if numPrerequisites[i] == 0]
        i = 0
        while i < len(res) < numCourses:
            course = res[i]
            i += 1
            for nextCourse in courses[course]:
                numPrerequisites[nextCourse] -= 1
                if numPrerequisites[nextCourse] == 0:
                    res.append(nextCourse)

        return res if len(res) == numCourses else []