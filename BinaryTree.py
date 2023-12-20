class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def height(self, root):
        if root is None:
            return 0
        else:
            left_height = self.height(root.left)
            right_height = self.height(root.right)

        return max(left_height, right_height) + 1

    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False

        if value == node.data:
            return node, parent, True

        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)

        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False

    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj

        s, p, fl_find = self.__find(self.root, None, obj.data)

        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj

        return obj

    def show_tree(self, node):
        if node is None:
            return

        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)

    def show_tree_post_order(self, node):
        if node is None:
            return

        self.show_tree(node.right)
        print(node.data)
        self.show_tree(node.left)

    def show_wide_tree(self, node):
        if node is None:
            return

        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.data, end=' ')
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            print()
            v = vn

    def __deal_leaf(self, s, p):
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None

    def __find_min(self, node, parent):
        if node.left:
            return self.__find_min(node.left, node)
        return node, parent

    def __del_one_child(self, s, p):
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left

    def del_node(self, key):
        s, p, fl_find = self.__find(self.root, None, key)
        if not fl_find:
            return None
        if s.left is None and s.right is None:
            self.__deal_leaf(s, p)
        elif s.left is None or s.right is None:
            self.__del_one_child(s, p)
        else:
            sr, pr = self.__find_min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)

    def is_balanced(self, root):
        def height(node):
            if node is None:
                return 0
            return 1 + max(height(node.left), height(node.right))

        def is_balanced_recursive(node):
            if node is None:
                return True, 0

            left_balanced, left_height = is_balanced_recursive(node.left)
            right_balanced, right_height = is_balanced_recursive(node.right)

            current_balanced = abs(left_height - right_height) <= 1
            current_height = 1 + max(left_height, right_height)

            return current_balanced and left_balanced and right_balanced, current_height

        balanced, _ = is_balanced_recursive(root)
        return balanced

    def arr_to_balanced_tree(self, arr):
        if not arr:
            return None

        mid = len(arr) // 2
        root = Node(arr[mid])
        root.left = self.arr_to_balanced_tree(arr[:mid])
        root.right = self.arr_to_balanced_tree(arr[mid + 1:])
        return root

    def find_lca(self, root, p, q):
        if root is None:
            return None

        if root.data == p.data or root.data == q.data:
            return root

        left_lca = self.find_lca(root.left, p, q)
        right_lca = self.find_lca(root.right, p, q)

        if left_lca and right_lca:
            return root

        return left_lca if left_lca else right_lca

    def are_indetical(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        elif root1 is not None and root2 is not None:
            return (
                    root1.data == root2.data
                    and self.are_indetical(root1.left, root2.left)
                    and self.are_indetical(root1.right, root2.right)
            )
        else:
            return False

    def max_depth(self, root):
        if root is None:
            return 0
        left_depth = self.max_depth(root.left)
        right_depth = self.max_depth(root.right)

        return max(left_depth, right_depth) + 1
