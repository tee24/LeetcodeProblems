#[[1,2],[3],[3],[]] -> [[0,1,3], [0,2,3]]
# DFS
class Solution:
    def allPathsSourceTarget(self, graph):
        ans = []

        def dfs(start_node, curr):
            for i in graph[start_node]:
                if i == len(graph)-1:
                    ans.append(curr+[i])
                    continue
                dfs(i, curr+[i])

        dfs(0, [0])

        return ans

# BFS
from queue import Queue
class Solution:
    def allPathsSourceTarget(self, graph):
        q = Queue()
        ans = []
        q.put([0])

        while q.qsize() > 0:
            vertex = q.get()

            if vertex[-1] == len(graph)-1:
                ans.append(vertex)
            else:
                for i in graph[vertex[-1]]:
                    q.put(vertex+[i])
        return ans


x = Solution()

print(x.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))
        