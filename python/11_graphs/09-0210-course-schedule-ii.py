from collections import defaultdict, deque
from typing import List


# Time:  O(m + n) where m is the number of edges and n is the number of courses
# Space: O(m + n)
class Solution:
    def findOrder(self, numCourses, prerequisites):
        courseToNextCourse = defaultdict(list)
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            courseToNextCourse[prereq].append(course)
            indegree[course] += 1

        q = deque([n for n in range(numCourses) if indegree[n] == 0])
        res = []
        while q:
            course = q.popleft()
            res.append(course)
            if course in courseToNextCourse:
                for nextCourse in courseToNextCourse[course]:
                    indegree[nextCourse] -= 1
                    if indegree[nextCourse] == 0:
                        q.append(nextCourse)

        return res if len(res) == numCourses else []
