def test_print_traversals(self):
    # WARNING:  Tests are for Print()
    # Debug calls to Print() in functions will cause failure

    stdout_ = sys.stdout  # Keep previous value
    sys.stdout = io.StringIO()

    self.bst = BinarySearchTree(1)
    self.bst.insert(8)
    self.bst.insert(5)
    self.bst.insert(7)
    self.bst.insert(6)
    self.bst.insert(3)
    self.bst.insert(4)
    self.bst.insert(2)

    self.bst.in_order_dft(self.bst)

    output = sys.stdout.getvalue()
    self.assertEqual(output, "1\n2\n3\n4\n5\n6\n7\n8\n")

    sys.stdout = io.StringIO()
    self.bst.bft_print(self.bst)
    output = sys.stdout.getvalue()
    self.assertEqual(output, "1\n8\n5\n3\n7\n2\n4\n6\n")

    sys.stdout = io.StringIO()
    self.bst.dft_print(self.bst)
    output = sys.stdout.getvalue()
    self.assertEqual(output, "1\n8\n5\n7\n6\n3\n4\n2\n")

    sys.stdout = io.StringIO()
    self.bst.pre_order_dft(self.bst)
    output = sys.stdout.getvalue()
    self.assertEqual(output, "1\n8\n5\n3\n2\n4\n7\n6\n")

    sys.stdout = io.StringIO()
    self.bst.post_order_dft(self.bst)
    output = sys.stdout.getvalue()
    self.assertEqual(output, "2\n4\n3\n6\n7\n5\n8\n1\n")

    sys.stdout = stdout_  # Restore stdout
