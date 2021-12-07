# Sample graph implementation
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = [] # Keeps track of visited nodes

def dfs(visited, graph, node):
    if node not in visited:
        print(node, " ")
        visited.append(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)

dfs(visited, graph, 'A') # DFS starting from A