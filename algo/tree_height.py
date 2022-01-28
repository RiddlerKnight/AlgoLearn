class BinaryNode:
    def __init__(self, left:int, right:int):
        self._left = left
        self._right = right

    @property
    def left(self):
        return self._left
    @property
    def right(self):
        return self._right

anode = BinaryNode(
    BinaryNode(
        BinaryNode(
            BinaryNode(
                BinaryNode(
                    BinaryNode(None,None),
                    None),
            None),
            BinaryNode(BinaryNode(
                BinaryNode(None,None),None),None))
        ,
        None)
    , 
    BinaryNode(None,
        BinaryNode(None,None))
    )


def find_node_height(node:BinaryNode):
    if node == None:
        return -1
    elif node.left == None and node.right == None :
        return 0
    
    return max(find_node_height(node.right), find_node_height(node.left)) + 1


print(find_node_height(anode))

print(max(10,20,2,3,50,2,2,3,4,5,12,5,6,665,23,41))

#print(find_node_height(nodes2))

