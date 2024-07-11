# 210. Course Schedule II

class Solution:
    visited = []
    on_path = []
    postorder_result = []
    has_cycle = False

    def build_graph(self, numCourses, prerequisites):
        g = dict()

        for i in range(numCourses):
            g[i] = []

        for edge in prerequisites:
            first = edge[1]
            second = edge[0]
            g[first].append(second)

        return g

    def traverse(self, graph, node):
        # check if cycle in graph
        if self.on_path[node]:
            self.has_cycle = True
            return

        # check if we have visited node or if there's no need to continue
        if self.visited[node] or self.has_cycle:
            return

        # pre-order operations
        self.visited[node] = True
        self.on_path[node] = True

        for child in graph[node]:
            self.traverse(graph, child)

        # post-order operations
        self.postorder_result.append(node)
        self.on_path[node] = False # unmark as on path
        return

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.visited = [False] * numCourses
        self.on_path = [False] * numCourses
        self.postorder_result = []

        graph = self.build_graph(numCourses, prerequisites)

        for i in range(numCourses):
            self.traverse(graph, i)

        # reverse ordering of postorder result
        result = self.postorder_result[::-1]

        return [] if self.has_cycle else result