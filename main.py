
import binary_tree
import make_list
import quick_sort
import sort_method
import merge_sort

import heap

for i in range(1,21):
    print(f'----------------------------------------------------------')
    un_sorted_list = make_list.make_random_list(1,20,7)
    print(f'{i}번째 횟수 입니다.')

    print(un_sorted_list,end='\n\n')

    method = sort_method.Sort_methods(un_sorted_list)

    print(f'insertion_sort:{method.insertion_sort()}')

    print(f'bubble_sort:{method.bubble_sort()}')

    print(f'selection_sort:{method.selection_sort()}')

    print(f'quick_sort:{ quick_sort.quick_sort(un_sorted_list,0,len(un_sorted_list)-1)}')

    print(f'merge_sort:{merge_sort.sort(0, len(un_sorted_list) - 1)}')

    print(f'heap_sort:{heap.heap_sort(un_sorted_list)}')

    root = binary_tree.Node(un_sorted_list[0])
    myTree = binary_tree.Binary_tree(root)

    datas = un_sorted_list
    nodes = [binary_tree.Node(data) for data in datas]

    for node in nodes:
        myTree.insert(node)

    print('이진트리')
    print(f'생성')
    print(myTree.bfs(myTree.root))
    print(f'찾기 {un_sorted_list[3]}')
    print('본인 노드'+myTree.search_node(myTree.root,un_sorted_list[3]).data)
    print('자식 노드'+myTree.search_parent_node(myTree.root,un_sorted_list[3]).data)
    print(f'삭제 {un_sorted_list[3]}')
    print(myTree.delete_node(myTree.root,un_sorted_list[3]))
    print(myTree.bfs(myTree.root))

    print(f'----------------------------------------------------------')




