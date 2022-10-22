
from collections import defaultdict
from tokenize import ContStr


#unweighted
def edgeToAdj(edgeList):

    adj = defaultdict()

    for x, y in edgeList:
        adj[x].append(y)
        adj[y].append(x)
    
    return adj

#weighted
def edgeToAdj(edgeList):

    adj = defaultdict()

    for x, y, cost in edgeList:
        adj[x].append((cost, y))
        adj[y].append((cost, x))
    
    return adj
