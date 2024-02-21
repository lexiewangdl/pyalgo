# 797.

class Solution:
    result = []
    graph = []

    def traverse(self, path, s):
        # Add node s to our path
        path.append(s)

        # If we found the target node
        if s == len(self.graph) - 1:
            # Make sure to create a copy of current path
            self.result.append(path.copy())

        # Traverse child nodes
        for n in self.graph[s]:
            self.traverse(path, n)

        # Remove node from path, should be outside of for loop
        path.pop()
        return

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.result = []
        self.graph = graph
        path = []
        self.traverse(path, 0)
        return self.result
