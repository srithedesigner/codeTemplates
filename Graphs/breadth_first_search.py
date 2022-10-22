
from asyncio import QueueEmpty
from collections import deque

from collections import deque

def breadthFirstSearch(adj, start):

    queue = deque()
    visited = set()

    queue.append(start)

    while len(queue) > 0:

        x = queue.popleft()
        if x in visited:
            continue

        visited.add(x)

        for nei in adj[x]:
            queue.append(nei)
    
    return
    