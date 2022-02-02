
graph = [[1,5,6],[0,4],[5],[5],[1],[0,2,3],[0]]

class TreeNode:
    def __init__(self, node_id, parent, children):
        self._node_id = node_id
        self._parent:TreeNode = parent
        self._children:list[TreeNode] = children

    # Node Id
    @property
    def Nodeid(self):
        return self._node_id
    @property
    def Parent(self):
        return self._parent
    @property
    def Children(self):
        return self._children


def root_tree(grp, root_id = 0):
    root = TreeNode(root_id, None, [])
    return build_tree(grp, root, None)

def build_tree(grp, node:TreeNode, parent:TreeNode):
    for child_id in grp[node.Nodeid]:
        if parent != None and child_id == parent.Nodeid:
            continue
        child = TreeNode(child_id, node, [])
        node.Children.append(child)
        build_tree(grp, child, node)
    return node

tree = root_tree(graph, 5)

print(tree)

