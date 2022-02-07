

def find_center(graph):
    all_node = len(graph)
    current_node_len = [None] * all_node
    leaves = []
    for i in range(0, all_node):
        current_node_len[i] = len(graph[i])
        if current_node_len[i] == 0 or current_node_len[i] == 1:
            leaves.append(i)
    leave_count = len(leaves)
    while leave_count < all_node:
        new_leaves = []
        for leave_node_index in leaves:
            for neighbor in graph[leave_node_index]:
                current_node_len[neighbor] = current_node_len[neighbor] - 1
                if current_node_len[neighbor] == 1:
                    new_leaves.append(neighbor)

            current_node_len[leave_node_index] = 0
            all_node = all_node - 1
        
        leave_count = len(new_leaves)
        leaves = new_leaves

    return leaves



graph =  [ [1], [0,2], [1,3,6,9], [2,4,5], [3], [3], [2,7,8], [6], [6], [2] ]
graph2 = [ [1], [0,2], [1,3,6,9], [2,4,5], [3], [3], [2,7,8], [6], [6], [2], [4], [5], [5]]

print(find_center(graph))
print(find_center(graph2))