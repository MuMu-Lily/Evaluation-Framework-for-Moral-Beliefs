from collections import defaultdict, deque

#根据graph找出图中最小的环，输出最小环中包含的结点
def find_min_cycle(graph):
    def dfs(node, visited, parent, cycle_start, cycle):
        nonlocal min_cycle

        visited[node] = True
        print("这轮的node:", node)
        cycle.append(node)

        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, visited, node, cycle_start, cycle)
                print("cycle:", cycle)

            elif neighbor != parent and neighbor == cycle_start and len(cycle) < len(min_cycle):
                min_cycle = cycle[:]
                print("min_cycle:", min_cycle)

        cycle.pop()

    min_cycle = []
    num_nodes = len(graph)
    visited = [False] * num_nodes

    for node in range(num_nodes):
        if not visited[node]:
            dfs(node, visited, -1, node, [])

    return min_cycle

 



def topological_sort(graph):
    in_degree = defaultdict(int)
    result = []
    
    # Calculate in-degrees for each letter
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    print("In-degree:", in_degree)
    # Initialize a queue with letters having in-degree 0
    queue = deque([node for node in graph if in_degree[node] == 0])
    
    # Perform topological sorting
    while queue:
        current = queue.popleft()
        result.append(current)
        
        # Update in-degrees and enqueue neighbors
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    print("Result:", result)
    print("graph:", graph)
    # Check for a cycle (if not all nodes are processed)
    if len(result) != len(graph): #存在环
        raise ValueError("The graph has a cycle, cannot perform topological sorting.")
    
    return result

def generate_graph(pairs):
    graph = defaultdict(list)
    for pair in pairs:
        graph[pair[0]].append(pair[1])
    return graph

if __name__ == "__main__":
    # pairs = [
    #     ('a', 'b'), ('a', 'e'), ('a', 'c'), ('e', 'd'),
    #     ('c', 'b'), ('b', 'd'), ('d', 'c'), ('e', 'j'),
    # ]

    # graph = generate_graph(pairs)
    # print("Graph:", graph)

    # try:
    #     result = topological_sort(graph)
    #     print("Topological Sorting Result:", result)
    # except ValueError as e:
    #     print(f"Error: {e}")
    # 例子
    graph = {
        0: [1],
        1: [2],
        2: [0]
    }
    
    min_cycle = find_min_cycle(graph)
    
    if min_cycle:
        print("最小环中的节点:", min_cycle)
    else:
        print("图中无环")
 