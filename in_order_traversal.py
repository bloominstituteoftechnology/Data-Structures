def in_order(n):
    if n is None:
        return

    in_order(n.left)

    print(n.value)

    in_order(n.right)
