# Sample graph implementation
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = [] # Visited node list
q = [] # Empty queue initialization

def bfs(visited, graph, node):
    visited.append(node)
    q.append(node)

    while q: # While the queue isn't empty
        n = q.pop(0) # Pops the first element off the queue
        print(n, " ")

        for neighbor in graph[n]:
            if neighbor not in visited:
                visited.append(neighbor)
                q.append(neighbor)

bfs(visited, graph, 'A') # BFS starting from A
