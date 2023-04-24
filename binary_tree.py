from collections import deque

class Node:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

class Binary_tree:
    def __init__(self,node=None):
        self.root = node

    # 삽입
    def insert(self,node:Node):
        return  self.insert_node(self.root,node)


    def insert_node(self,root:Node,node:Node):
        if root is None or node is None:
            return False
        else:
            if root.data <= node.data:
                if root.right is None:
                    root.right = node
                    return True
                self.insert_node(root.right,node)
            else :
                if root.left is None:
                    root.left = node
                    return True
                self.insert_node(root.left,node)

        return False
    # 검색
    def search_node(self,root,data): #DFS
        if root.data == data:
            return root
        elif root == None:
            return root
        else:
            if root.data <= data:
                return self.search_node(root.right,data)
            else :
                return self.search_node(root.left,data)

    def search_parent_node(self,root,data): #DFS
        if root.right == None :
            if root.left.data == data :
                return root
            else:
                return self.search_parent_node(root.left,data)
        elif root.left == None :
            if root.right.data == data :
                return root
            else:
                return self.search_parent_node(root.right,data)
        elif root.right.data == data or root.left.data == data:
            return root
        elif root == None:
            return root
        else:
            if root.data <= data and root.right != None:
                return self.search_parent_node(root.right,data)
            elif root.data > data and root.left != None :
                return self.search_parent_node(root.left,data)

    def find_dir(self,parent_node:Node,child_node:Node): # left->-1 , right->1
        if parent_node.left == None:
            return 1
        elif parent_node.right == None:
            return -1
        elif parent_node.left.data == child_node.data :
            return -1
        elif parent_node.right.data == child_node.data :
            return 1
        else:
            return 0

    def find_replaced_node(self,root:Node):
        if root.left == None :
            return root
        else:
            return self.find_replaced_node(root.left)

    # 삭제
    def delete_node(self,root:Node,data):
        # 삭제할 노드의 부모 노드까지 도달
        parent_node=self.search_parent_node(root,data)
        node = self.search_node(root,data)
        dir = self.find_dir(parent_node,node)
        print(f'parent_node:{parent_node.data} child:{node.data} dir:{dir}')
        # 삭제할 노드가 리프 노드일 경우
        if node.left==None and node.right==None:
            if dir == 1 :
                parent_node.right = None
            elif dir == -1:
                parent_node.left = None
            else:
                pass
        # 그냥 삭제하면됨
        # 삭제할 노드의 자식이 하나일 경우
        elif node.left == None :
            if dir == 1:
                parent_node.right = node.right
            elif dir == -1:
                parent_node.left = node.right
            else:
                pass
        elif node.right == None :
            if dir == 1:
                parent_node.right = node.left
            elif dir == -1:
                parent_node.left = node.left
            else:
                pass
        # 삭제할 노드가 자식이 둘일 경우
        else:
            replace_node = self.find_replaced_node(node.right) # 대체 노드를 선정
            self.delete_node(root,replace_node.data)
            if dir == 1:
                parent_node.right = replace_node
            elif dir == -1:
                parent_node.left = replace_node
            else:
                pass
            print(replace_node.data)
            replace_node.left = node.left
            replace_node.right = node.right

    # 출력
    def bfs(self,root):
        result =[[]]
        if root is None:
            return 0

        queue = deque([root])
        depth = 0

        while queue:
            depth+=1
            for _ in range(len(queue)):
                cur_node = queue.popleft()
                if cur_node =='_':
                    result[0].append('_')
                    continue

                result[0].append(cur_node.data)

                if cur_node.left:
                    queue.append(cur_node.left)
                else:
                    queue.append('_')

                if cur_node.right:
                    queue.append(cur_node.right)
                else:
                    queue.append('_')

        result.append(depth-1)

        return result


root = Node(50)
myTree = Binary_tree(root)

datas =[17,72,12,23,54,76,9,14,20,25,67,18,21,29]
nodes = [Node(data) for data in datas]

for node in nodes :
    myTree.insert(node)

print(myTree.bfs(myTree.root))
#print(myTree.search_node(myTree.root,23).data)
#print(myTree.search_parent_node(myTree.root,21).data)
print(myTree.delete_node(myTree.root,23))
print(myTree.bfs(myTree.root))
#print(myTree.bfs(myTree.root))















