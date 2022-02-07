
def generate_tree(level, element, leaf:list):
    if level != 0:
        for i in element:
            leaf.append(i)
            generate_tree(level - 1, element, leaf[i])
    #else:
        
        #leaf.append()
            
    return leaf

def create_tree(level, element):
    allLeaf = [[]]
    generate_tree(level, element, allLeaf)
    # for i in range(1, element + 1):
    #     generate_tree(level, element, allLeaf[i])

    return allLeaf


create_tree(2,4)