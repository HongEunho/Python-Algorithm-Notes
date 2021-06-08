class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self, root):
        self.root = root

    ## 자신의 자리를 찾아 탐색하여 들어감
    def insert(self, value):
        self.current_node = self.root
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        self.current_node = self.root
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif self.current_node.value > value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False

    def delete(self, value):
        ## 삭제할 노드가 있는지 검사하여 없으면 False 리턴
        ## 검사 후에는, 삭제할 노드가 current_node가 되고 삭제할 노드의 부모가 parent가 된다.
        is_search = False
        self.current_node = self.root
        self.parent = self.root
        while self.current_node:
            if self.current_node.value == value:
                is_search = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right

        if is_search == False:
            return False

        ## 삭제할 노드가 자식 노드를 갖고 있지 않을 때
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None

        ## 삭제할 노드가 자식 노드를 한 개 가지고 있을 때(왼쪽 자식 노드)
        if self.current_node != None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left

        ## 삭제할 노드가 자식 노드를 한 개 가지고 있을 때(오른쪽 자식 노드)
        if self.current_node.left == None and self.current_node.right != None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right

        ## 삭제할 노드가 자식 노드를 두 개 가지고 있을 때
        if self.current_node.left != None and self.current_node.right != None:
            self.change_node = self.current_node.right
            self.change_node_parent = self.current_node.right
            while self.change_node.left != None:
                self.change_node_parent = self.change_node
                self.change_node = self.change_node.left
            if self.change_node.right != None:
                self.change_node_parent.left = self.change_node.right
            else:
                self.change_node_parent.left = None

            if value < self.parent.value:
                self.parent.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.current_node.left
            else:
                self.parent.right = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right

            return True