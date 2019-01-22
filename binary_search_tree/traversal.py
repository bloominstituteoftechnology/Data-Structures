def in_order(n):

    if n == None:
        return

    in_order(n.left)

    print(n.value)

    in_order(n.right)


def pre_order(n):

    if n == None:
        return

    print(n.value)

    in_order(n.left)

    in_order(n.right)


def post_order(n):

    if n == None:
        return

    in_order(n.left)

    in_order(n.right)

    print(n.value)
