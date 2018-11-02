import unittest
from pennant import Pennant

class PennantTests(unittest.TestCase):
    def setUp(self):
        self.pennant = Pennant()

    def test_combining_two_one_element_pennants(self):
        other_pennant = Pennant()
        self.pennant.combine(other_pennant)

        self.assertEqual(self.pennant.middle, other_pennant)
        self.assertEqual(self.pennant.count, 2)
        self.assertEqual(self.pennant.k, 1)
        self.assertIsNone(self.pennant.left)
        self.assertIsNone(self.pennant.right)

    def test_combining_two_two_element_pennants(self):
        self.pennant.combine(Pennant())
        other_pennant = Pennant()
        other_pennant.combine(Pennant())
        self.pennant.combine(other_pennant)

        self.assertEqual(self.pennant.middle, other_pennant)
        self.assertEqual(self.pennant.count, 4)
        self.assertEqual(self.pennant.k, 2)
        self.assertIsNone(self.pennant.left)
        self.assertIsNone(self.pennant.right)

    def test_combining_two_four_element_pennants(self):
        self.pennant.combine(Pennant())
        pennant_1 = Pennant()
        pennant_1.combine(Pennant())
        self.pennant.combine(pennant_1)

        pennant_2 = Pennant()
        pennant_3 = Pennant()

        pennant_2.combine(Pennant())
        pennant_3.combine(Pennant())

        pennant_2.combine(pennant_3)

        self.pennant.combine(pennant_2)

        self.assertEqual(self.pennant.middle, pennant_2)
        self.assertEqual(self.pennant.count, 8)
        self.assertEqual(self.pennant.k, 3)
        self.assertIsNone(self.pennant.left)
        self.assertIsNone(self.pennant.right)

    def test_splitting_one_two_element_pennant(self):
        self.pennant.combine(Pennant())
        new_pennant = self.pennant.split()

        self.assertIsNone(self.pennant.middle)
        self.assertIsNone(self.pennant.left)
        self.assertIsNone(self.pennant.right)
        self.assertEqual(self.pennant.count, 1)
        self.assertEqual(self.pennant.k, 0)

        self.assertIsNone(new_pennant.middle)
        self.assertIsNone(new_pennant.left)
        self.assertIsNone(new_pennant.right)
        self.assertEqual(new_pennant.count, 1)
        self.assertEqual(new_pennant.k, 0)

    def test_splitting_one_four_element_pennant(self):
        pennant_1 = Pennant()
        pennant_2 = Pennant()
        pennant_3 = Pennant()

        self.pennant.combine(pennant_2)
        pennant_1.combine(pennant_3)
        self.pennant.combine(pennant_1)

        new_pennant = self.pennant.split()

        self.assertEqual(self.pennant.middle, pennant_2)
        self.assertEqual(new_pennant.middle, pennant_3)
        self.assertEqual(self.pennant.count, 2)
        self.assertEqual(new_pennant.count, 2)
        self.assertEqual(self.pennant.k, 1)
        self.assertEqual(new_pennant.k, 1)
        self.assertIsNone(self.pennant.left)
        self.assertIsNone(self.pennant.right)
        self.assertIsNone(new_pennant.left)
        self.assertIsNone(new_pennant.right)


if __name__ == '__main__':
    unittest.main()