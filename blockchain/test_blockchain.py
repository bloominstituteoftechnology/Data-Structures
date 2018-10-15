import time
import hashlib
import unittest
from blockchain import Block, BlockChain

class BlockChainTests(unittest.TestCase):
  def setUp(self):
    self.chain = BlockChain()

  def test_is_valid_block_structure_correctness(self):
    valid_block = Block(1, 'hash', 'previous_hash', int(round(time.time() * 1000)), 'data')
    invalid_block = Block(2, 'next_hash', 'hash', str(round(time.time() * 1000)), 'more data')
    
    self.assertTrue(valid_block.is_valid_block_structure())
    self.assertFalse(invalid_block.is_valid_block_structure())

  def test_is_valid_genesis_correctness(self):
    genesis = self.chain.get_latest_block()
    fake_genesis = Block(0, hashlib.sha256(str(round(time.time() * 1000)).encode('utf-8') + b"The Genesis block"), None, int(round(time.time() * 1000)), "The Genesis block")

    self.assertTrue(self.chain.is_valid_genesis(genesis))
    self.assertFalse(self.chain.is_valid_genesis(fake_genesis))

  def test_is_valid_new_block_correctness(self):
    new_block = Block(1, hashlib.sha256(str(round(time.time() * 1000)).encode('utf-8') + b"The next block"), self.chain.get_latest_block().hash, int(round(time.time() * 1000)), "The next block")
    self.assertTrue(self.chain.is_valid_new_block(new_block, self.chain.get_latest_block()))

  def test_add_block_adds_new_block(self):
    pass

  def test_generate_next_block_correctness(self):
    pass
    # next_block = self.chain.generate_next_block('new data')
    # self.assertTrue(next_block.is_valid_block_structure())
    # self.assertTrue(self.chain)


if __name__ == '__main__':
  unittest.main()