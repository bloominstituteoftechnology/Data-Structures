"""
    1. Recursion - process of repeating items in a self-similar way || basically reduce a problem
    into to smaller problems || not good to have infinite recursion
    2. BST
    3. Traversal
    4. Heap
"""


def mult(a, b):
    if b == a:
        return a
    else:
        return a + mult(a, b - 1)


print(mult(1, 2))