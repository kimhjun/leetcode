class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        num_nodes = len(isConnected)
        total_nodes = list(range(num_nodes))

        import random
        visited = set()
        count = 0
        while total_nodes:
            num_nodes = len(total_nodes)
            idx = random.randint(0, num_nodes-1)
            idx_row = total_nodes[idx]
            row = isConnected[idx_row]
            for idx_to, val in enumerate(row):
                if val == 1:
                    total_nodes.remove(idx_to)
                    visited.add(idx_to)
            
            while visited:
                newly_visited = set()
                for city in visited:
                    row = isConnected[city]
                    for idx_to, val in enumerate(row):
                        if val == 1 and idx_to in total_nodes:
                            total_nodes.remove(idx_to)
                            newly_visited.add(idx_to)
                visited = newly_visited
            count += 1
        return count