

from enum import unique


S = ["ATG", "GGG", "GGT", "GTA", "GTG", "TAT", "TGG"]


def find_all_node(s):
    s_list = set()
    for item in s:
        s_list.add(item[:2])
        s_list.add(item[1:3])
    return s_list


def sbh(s):
    first_node = None
    for item in s:
        match_flag: bool
        front = item[:2]
        for compairer in s:
            back = compairer[1:3]
            if front == back:
                match_flag = True
        if match_flag == False:
            first_node = front
    if first_node == None:
        first_node = s[0][:2]

    all_node = find_all_node(s)
    nod_ref = find_all_node(s)

    # find first node and remove
    node_seq = []
    for item in all_node:
        if item == first_node:
            node_seq.append(item)
            nod_ref.remove(item)
    while len(nod_ref) != 0:
        ix = 0
        for item in s:
            for left in nod_ref:
                if ix != len(s) and s[ix][1:3] == left:
                    node_seq.append(left)
                    nod_ref.remove(left)
                    break
                ix += 1
    return


result = find_all_node(S)
print(result)

sbh(S)
