import time
import unittest
from blockchain import Block, BlockChain

class BlockChainTests(unittest.TestCase):
  def setUp(self):
    self.chain = BlockChain()

  def test_is_valid_block_structure(self):
    valid_block = Block(1, 'hash', 'previous_hash', int(round(time.time() * 1000)), 'data')
    invalid_block = Block(2, 'next_hash', 'hash', str(round(time.time() * 1000)), 'more data')
    self.assertTrue(valid_block.is_valid_block_structure())
    self.assertFalse(invalid_block.is_valid_block_structure())

  


if __name__ == '__main__':
  unittest.main()