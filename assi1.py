class Graph:

    def __init__(self, vertices):
        self.Graph = {}
        for i in range(vertices):
            self.Graph[i] = []

    def addEdge(self, u, v):
        self.Graph[u].append(v)
        self.Graph[v].append(u)

    def DFS(self, start):
        visited = set()
        visited.add(start)
        print(start, end=" ")
        for vertex in self.Graph[start]:
            if vertex not in visited:
                self.DFSfunc(vertex, visited)

    def DFSfunc(self, v, visited):
        visited.add(v)
        print(v, end=" ")
        for neighbour in self.Graph[v]:
            if neighbour not in visited:
                self.DFSfunc(neighbour, visited)

    def BFS(self, s):
        visited = [False] * (max(self.Graph) + 1)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            for i in self.Graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


vertices = int(input("\nEnter no. of vertices : "))
edges = int(input("\nEnter no. of edges : "))

g = Graph(vertices)

for i in range(edges):
    print("\nEnter vertices of the ", i, " edge:")
    u = int(input())
    v = int(input())
    g.addEdge(u, v)

run = True
while (run):
    choice = int(input("\n\n1. DFS\n2. BFS\n0. Exit\nEnter choice: "))
    if (choice == 1):
        start = int(input("\nEnter starting node : "))
        print("DFS:", end=" ")
        g.DFS(s)
    elif (choice == 2):
        start = int(input("\nEnter starting node : "))
        print("\nBFS:", end=" ")
        g.BFS(start)
    elif (choice == 0):
        run = False
    else:
        print("Enter valid choice")

assig 1.py
