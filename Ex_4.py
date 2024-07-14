# Напишите функцию для проверки симметричности двоичного дерева.

# Дерево 1:
#         1
#        / \
#       /   \
#      2     2
#     / \   / \
#    3   4 4   3
# 
# Дерево 2:
#         1
#        / \
#       /   \
#      2     2
#     / \   / \
#    3   5 6   3
# 
# Дерево 3:
#         1
#        / \
 #      /   \
#      2     2
#     /       \
#    5         5


def is_tree_symmetric(tree):
    def check_symmetric(subtree_0, subtree_1):
        if not subtree_0 and not subtree_1:
            return True
        elif subtree_0 and subtree_1:
            return (subtree_0.data == subtree_1.data
                    and check_symmetric(subtree_0.left, subtree_1.right)
                    and check_symmetric(subtree_0.right, subtree_1.left))
        return False
    return not tree or check_symmetric(tree.left, tree.right)



# Пример использования с заданными в условии деревьями:

from collections import namedtuple
Node = namedtuple('Node', ['data', 'left', 'right'])

tree1 = Node(1, Node(2, Node(3, None, None), Node(4, None, None)), Node(2, Node(4, None, None), Node(3, None, None)))
tree2 = Node(1, Node(2, Node(3, None, None), Node(5, None, None)), Node(2, Node(6, None, None), Node(3, None, None)))
tree3 = Node(1, Node(2, Node(5, None, None), None), Node(2, None, Node(5, None, None)))
           
for t in [tree1, tree2, tree3]:
  print(is_tree_symmetric(t))
