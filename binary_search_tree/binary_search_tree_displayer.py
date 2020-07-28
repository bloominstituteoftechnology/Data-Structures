# display source code: https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python

class BSTDisplayer:
    def __init__(self, bst):
        self.bst = bst
    
    def display(self):
        lines, *_ = self._display_aux(self.bst)
        for line in lines:
            print(line)

    def _display_aux(self, bst_node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if bst_node.right is None and bst_node.left is None:
            line = '%s' % bst_node.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if bst_node.right is None:
            lines, n, p, x = self._display_aux(bst_node.left)
            s = '%s' % bst_node.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if bst_node.left is None:
            lines, n, p, x = self._display_aux(bst_node.right)
            s = '%s' % bst_node.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_aux(bst_node.left)
        right, m, q, y = self._display_aux(bst_node.right)
        s = '%s' % bst_node.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2