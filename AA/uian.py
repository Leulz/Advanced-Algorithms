def dfs(node, color, node_colors):
    node_colors[node] = color
    for child in village_graph[node]:
        if node_colors[child] != color:
            dfs(child, color, node_colors)

def satisfiable():
    node_colors = [-1] * num_places

    components_with_odd_parity = 0
    color = 0
    for node in range(num_places):
        if node_colors[node] == -1:
            dfs(node, color, node_colors)

            for node_aux in range(num_places):
                if node_colors[node_aux] == color and parity[node_aux] == 1:
                    components_with_odd_parity += 1
                    break

            color += 1

    if components_with_odd_parity > 1:
        return False
    else:
        return True

def read_village_graph():
    for i in range(num_roads):
        orig, dest = map(int, raw_input().split())
        village_graph[orig - 1].append(dest - 1)
        village_graph[dest - 1].append(orig - 1)

def calculate_root():
    for i in range(num_places):
        if parity[i] == 1:
            return i
    return 0

def needToCorrectParity(node):
    return (new_parity[node] % 2 == 1 and parity[node] == 0) or (new_parity[node] % 2 == 0 and parity[node] == 1)

def solve_path(node, parent):
    visit[node] = True
    path.append(node + 1)
    new_parity[node] += 1

    for child in village_graph[node]:
        if not visit[child]:
            solve_path(child, node)
            path.append(node + 1)
            new_parity[node] += 1

    if needToCorrectParity(node) and parent != -1:
        path.append(parent + 1)
        new_parity[parent] += 1
        path.append(node + 1)
        new_parity[node] += 1


num_places, num_roads = map(int, raw_input().split())
village_graph = [[] for i in range(num_places)]
read_village_graph()
parity = map(int, raw_input().split())

path = []
new_parity = [0] * num_places
visit = [False] * num_places
if satisfiable():
    visit = [False] * num_places
    root = calculate_root()
    solve_path(root, -1)
    
    if needToCorrectParity(root):
        path.pop()

    print len(path)
    if len(path) != 0:
        print ' '.join(map(str, path))
else:
    print -1
