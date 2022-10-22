
from collections import deque

def depthFirstSearch(adj, start):

    stack = deque()
    visited = set()

    stack.append(start)

    while len(stack) > 0:

        x = stack.pop()
        if x in visited:
            continue

        visited.add(x)

        for nei in adj[x]:
            stack.append(nei)
    
    return
    