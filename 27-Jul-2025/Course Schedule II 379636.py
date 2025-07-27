# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build the adjacency lists
        adj=defaultdict(list)
        for tar, src in prerequisites:
            adj[src].append(tar)
        # declarate the visit set, courses, and path set
        visit, path, courses= set(), set(), []
        # run the dfs for all the courses
        for i in range(numCourses):
            if not self.dfs(i, adj, visit, courses, path):
                return []
            # check if dfs returns false
            # if it's false return []
        courses.reverse()
        # reverse the course and return it
        return courses
    def dfs(self, src, adj, visit, courses, path):
        # IMPLEMENTATION for the dfs method
        # it should accept 5 parameters(src, tar, visit, course, path)
        # check if the src in path if it's true return False
        if src in path:
            return False
        if src in visit:
            return True
        # check if it's in the visit set and if's true return True
        # And add the src to the path if it's not in the path
        # add the src to the visit set if itsn't in the set
        path.add(src)
        visit.add(src)
        for neighbour in adj[src]:
            # run the dfs for all the neighbours and check if the result is false
            if not self.dfs(neighbour, adj, visit, courses, path):
                return False
        courses.append(src)
        # add the course to the courses list and remove it from the path
        path.remove(src)
        return True