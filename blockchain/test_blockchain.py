import time
import hashlib
import unittest
from blockchain import Block, BlockChain

class BlockChainTests(unittest.TestCase):
  def setUp(self):
    self.chain = BlockChain()

  def test_is_valid_genesis_correctness(self):
    genesis = self.chain.get_latest_block()
    fake_genesis = Block(0, hashlib.sha256(str(round(time.time() * 1000)).encode('utf-8') + b"The Genesis block"), None, int(round(time.time() * 1000)), "The Genesis block")

    self.assertTrue(self.chain.is_valid_genesis(genesis))
    self.assertFalse(self.chain.is_valid_genesis(fake_genesis))

  def test_is_valid_new_block_correctness(self):
    timestamp = str(round(time.time() * 1000))
    previous_block = self.chain.get_latest_block()
    correct_block = Block(1, self.chain.calculate_hash(1, previous_block.hash, timestamp, "The correct block"), self.chain.get_latest_block().hash, int(round(time.time() * 1000)), "The correct block")
    incorrect_index = Block(2, self.chain.calculate_hash(2, previous_block.hash, timestamp, "The incorrect block"), self.chain.get_latest_block().hash, int(round(time.time() * 1000)), "The incorrect block")
    incorrect_hash = Block(1, self.chain.calculate_hash(1, hashlib.sha256('hi'.encode('utf-8')).hexdigest(), timestamp, "The correct block"), self.chain.get_latest_block().hash, int(round(time.time() * 1000)), "The correct block") 

    self.assertTrue(self.chain.is_valid_new_block(correct_block, self.chain.get_latest_block()))
    self.assertFalse(self.chain.is_valid_new_block(incorrect_index, self.chain.get_latest_block()))
    self.assertFalse(self.chain.is_valid_new_block(incorrect_hash, self.chain.get_latest_block()))

  def test_generate_next_block_correctness(self):
    next_block = self.chain.generate_next_block('new data')
    previous_block = self.chain.get_latest_block()

    self.assertEqual(next_block.data, 'new data')
    self.assertEqual(next_block.index, previous_block.index + 1)
    self.assertEqual(next_block.hash, self.chain.calculate_hash(next_block.index, previous_block.hash, next_block.timestamp, next_block.data))
    
  def test_adding_correct_block(self):
    next_block = self.chain.generate_next_block('new data')
    self.chain.add_block(next_block)

    latest_block = self.chain.get_latest_block()

    self.assertEqual(len(self.chain), 2)
    self.assertEqual(latest_block.index, next_block.index)
    self.assertEqual(latest_block.hash, next_block.hash)
    self.assertEqual(latest_block.data, next_block.data)
    self.assertEqual(latest_block.timestamp, next_block.timestamp)
    self.assertEqual(latest_block.previous_hash, next_block.previous_hash)

  def test_adding_incorrect_block(self):
    next_block = self.chain.generate_next_block('new data')
    self.chain.add_block(next_block)

    incorrect_block = Block(2, hashlib.sha256('wrong'.encode('utf-8')).hexdigest(), next_block.hash, int(round(time.time() * 1000)), "Not correct block")
    self.chain.add_block(incorrect_block)

    self.assertEqual(len(self.chain), 2)
    

if __name__ == '__main__':
  unittest.main()