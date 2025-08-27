class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        rank = [1]*(n+1)
        parent = [i for i in range(n+1)]

        def find(node):
            if node == parent[node]:
                return parent[node]
            parent[node] = find(parent[node])
            return parent[node]

        def union(u,v):
            parent_u = find(u)
            parent_v = find(v)

            if parent_u == parent_v:
                return False

            if rank[parent_u] < rank[parent_v]:
                parent[parent_u] = parent[v]
                rank[parent_v] += rank[parent_u]

            else:
                parent[parent_v] = parent_u
                rank[parent_u] += rank[parent_v]

            return True

        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]
