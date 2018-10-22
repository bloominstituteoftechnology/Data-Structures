import unittest
from penant import Penant

class PenantTests(unittest.TestCase):
    def setUp(self):
        self.penant = Penant()

    def test_combining_two_one_element_penants(self):
        other_penant = Penant()
        self.penant.combine(other_penant)

        self.assertEqual(self.penant.middle, other_penant)
        self.assertEqual(self.penant.count, 2)
        self.assertEqual(self.penant.k, 1)
        self.assertIsNone(self.penant.left)
        self.assertIsNone(self.penant.right)

    def test_combining_two_two_element_penants(self):
        self.penant.combine(Penant())
        other_penant = Penant()
        other_penant.combine(Penant())
        self.penant.combine(other_penant)

        self.assertEqual(self.penant.middle, other_penant)
        self.assertEqual(self.penant.count, 4)
        self.assertEqual(self.penant.k, 2)
        self.assertIsNone(self.penant.left)
        self.assertIsNone(self.penant.right)

    def test_combining_two_four_element_penants(self):
        self.penant.combine(Penant())
        penant_1 = Penant()
        penant_1.combine(Penant())
        self.penant.combine(penant_1)

        penant_2 = Penant()
        penant_3 = Penant()

        penant_2.combine(Penant())
        penant_3.combine(Penant())

        penant_2.combine(penant_3)

        self.penant.combine(penant_2)

        self.assertEqual(self.penant.middle, penant_2)
        self.assertEqual(self.penant.count, 8)
        self.assertEqual(self.penant.k, 3)
        self.assertIsNone(self.penant.left)
        self.assertIsNone(self.penant.right)

    def test_splitting_one_two_element_penant(self):
        self.penant.combine(Penant())
        new_penant = self.penant.split()

        self.assertIsNone(self.penant.middle)
        self.assertIsNone(self.penant.left)
        self.assertIsNone(self.penant.right)
        self.assertEqual(self.penant.count, 1)
        self.assertEqual(self.penant.k, 0)

        self.assertIsNone(new_penant.middle)
        self.assertIsNone(new_penant.left)
        self.assertIsNone(new_penant.right)
        self.assertEqual(new_penant.count, 1)
        self.assertEqual(new_penant.k, 0)

    def test_splitting_one_four_element_penant(self):
        penant_1 = Penant()
        penant_2 = Penant()
        penant_3 = Penant()

        self.penant.combine(penant_2)
        penant_1.combine(penant_3)
        self.penant.combine(penant_1)

        new_penant = self.penant.split()

        self.assertEqual(self.penant.middle, penant_2)
        self.assertEqual(new_penant.middle, penant_3)
        self.assertEqual(self.penant.count, 2)
        self.assertEqual(new_penant.count, 2)
        self.assertEqual(self.penant.k, 1)
        self.assertEqual(new_penant.k, 1)
        self.assertIsNone(self.penant.left)
        self.assertIsNone(self.penant.right)
        self.assertIsNone(new_penant.left)
        self.assertIsNone(new_penant.right)


if __name__ == '__main__':
    unittest.main()