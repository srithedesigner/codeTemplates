class UnionFind:

    def __init__(self):
        self.parent = {}
        self.size = {}

    def find(self, x):

        if x not in self.parent:
            self.parent[x] = x
            self.size[x] = 1
        
        if x == self.parent[x]:
            return x
        
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):

        x, y = self.find(x), self.find(y)
        if x == y:
            return True

        if self.size[x] > self.size[y]:
            x, y = y, x
        
        self.parent[x] = y
        self.size[y] += self.size[x]

        return True