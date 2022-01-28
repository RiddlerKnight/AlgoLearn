
node = [6,
            [
                5,[3,6],
                7,[-8,[-6],10],
                12,[3,[5,[9,7,[-8,-7,[10]]]]]
            ]
    ]

def search_and_add(node):
    node_sum = 0
    # if(node == None):
    #     return 0
    for n in node:
        if type(n) is int:
            node_sum += n
            continue
        node_sum += search_and_add(n)
    return node_sum

print(search_and_add(node))
