arr = [19, 17, 13, 13, 4]


def sort(left, right):
    mid = (left + right) // 2
    print(f'left:{left} right:{right}')
    if left == right:
        return [arr[left]]

    left_node = sort(left, mid)
    right_node = sort(mid + 1, right)

    return merge(left_node, right_node)


def merge(l_node, r_node):
    temp = []
    pointer_l = 0
    pointer_r = 0

    while pointer_l < len(l_node) and pointer_r < len(r_node):
        l_val, r_val = l_node[pointer_l], r_node[pointer_r]
        if l_val < r_val:
            temp.append(l_val)
            pointer_l += 1
        else:
            temp.append(r_val)
            pointer_r += 1

    if pointer_l == len(l_node):
        temp.extend(r_node[pointer_r:])
    else:
        temp.extend(l_node[pointer_l:])

    return temp

    print(f'temp:{r_node}')
    return temp


print(sort(0, len(arr) - 1))
