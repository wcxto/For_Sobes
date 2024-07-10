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
