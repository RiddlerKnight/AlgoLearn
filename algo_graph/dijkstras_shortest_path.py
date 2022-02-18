

def FindShortPath(gp, start, end):
    # node = len(gp)
    passed_node = []    
    path = []

    # Find the end node is in the passed node
    while passed_node.count(end) != 1:
        new_start = 0
        index = 0
        # Fetch weight of start node
        for node_arr in gp[start]:
            # if current node is the end node, end loop
            if start == end:
                # path.append(node_arr)
                break
            if len(path) == 0 or len(path) == len(passed_node):
                    path.append([])
            if (path[len(path) - 1] == [] or (node_arr[1] < path[len(path) - 1][1])) and passed_node.count(start) == 0 and passed_node.count(node_arr[0]) == 0:
                path[len(path) - 1] = node_arr
                new_start = node_arr[0]
            index += 1

        passed_node.append(start)
        start = new_start
        
    return path



weight = [
    [[1,5],[2,3]],
    [[0,5],[2,2],[3,4],[4,6]],
    [[0,3],[1,2],[3,5],[4,3]],
    [[1,4],[2,5],[4,3],[5,1]],
    [[2,3],[1,6],[3,3],[5,1]],
    [[3,1],[4,1]],
]

print(FindShortPath(weight,0,5))
