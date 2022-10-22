import heapq
from collections import defaultdict

def dijkstra(adj, start, n):

    visited = set()
    heap = [(0, start)]
    distances = defaultdict(lambda : float('inf'))
    distances[start] = 0

    while heap:

        curr_distance, curr_node = heapq.heappop(heap)
        visited.add(curr_node)

        if len(visited) == n:
            return distances
        
        for dist, adj_node in adj[curr_node]:
            if adj_node not in visited:
                
                new_dist = distances[curr_node] + dist
                if new_dist < distances[adj_node]:
                    distances[adj_node] = new_dist
                    heapq.heappush(heap, (new_dist, adj_node))
    
    return distances
