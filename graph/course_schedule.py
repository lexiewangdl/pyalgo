# 207. Course Schedule

class Solution:
    visited = []
    on_path = []
    result = True

    def build_graph(self, numCourses, prerequisites):
        # use adjacency list to implement graph
        graph = dict()

        for i in range(numCourses):
            graph[i] = []  # initialize empty lists

        for edge in prerequisites:  # O(N)
            start_node = edge[1]  # curr course
            end_node = edge[0]  # prereq

            # add edge to graph
            graph[start_node].append(end_node)

        return graph

    def traverse(self, graph, node):
        # use DFS traversal
        if self.on_path[node]:
            self.result = False
            return

        if self.visited[node]:
            return

        # pre-order traversal
        self.visited[node] = True  # mark node as visited
        self.on_path[node] = True

        for child in graph[node]:
            self.traverse(graph, child)

        # post-order travelsal
        self.on_path[node] = False
        return

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # initialize graph
        g = self.build_graph(numCourses, prerequisites)

        self.visited = [False] * numCourses
        self.on_path = [False] * numCourses
        self.result = True

        # traverse the graph
        # not all nodes are connected, there are separate sequences of classes
        # the sequences might not be related to one another
        # thus, use for loop to use every single node as start node
        for i in range(numCourses):
            self.traverse(g, i)

        return self.result