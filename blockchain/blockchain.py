import time
import hashlib

class Block:
  def __init__(self, index, hash, previous_hash, timestamp, data):
    self.index = index
    self.hash = hash
    self.previous_hash = previous_hash
    self.timestamp = timestamp
    self.data = data

  def __repr__(self):
    return "Block(" + str(self.index) + "," + str(self.hash) + "," + str(self.previous_hash) + "," + str(self.timestamp) + "," + str(self.data)

  def is_valid_block_structure(self):
    return isinstance(self.index, int) and isinstance(self.hash, str) and isinstance(self.previous_hash, str) and isinstance(self.timestamp, int) and isinstance(self.data, str)

class Chain:
  def __init__(self):
    self.blocks = [Block(0, '816534932c2b7154836da6afc367695e6337db8a921823784c14378abed4f7d7', None, 1465154705, 'my genesis block!!')]

  def __len__(self):
    return len(self.blocks)

  def add_block(self, new_block):
    if self.is_valid_new_block(new_block):
      self.chain.append(new_block)

  def get_latest_block(self):
    return self.blocks[-1]

  def calculate_hash_for_block(self, new_block):
    return hashlib.sha256(new_block.index + new_block.previous_hash + new_block.timestamp + new_block.data).hexdigest()

  def generate_next_block(self, block_data):
    previous_block = self.get_latest_block()
    next_index = previous_block.index + 1
    next_timestamp = int(round(time.time() * 1000))
    next_hash = self.calculate_hash_for_block(next_index, previous_block.hash, next_timestamp, block_data)
    return Block(next_index, next_hash, previous_block.hash, next_timestamp, block_data)

  def is_valid_new_block(self, new_block, previous_block):
    if not new_block.is_valid_block_structure():
      print('invalid block structure')
      return False
    if previous_block.index + 1 != new_block.index:
      print('invalid index')
      return False
    if previous_block.hash != new_block.previous_hash:
      print('invalid previous hash')
      return False
    if self.calculate_hash_for_block(new_block) != new_block.hash:
      print('hashes do not match')
      return False
    return True

  def is_valid_chain(self, new_chain):
    is_valid_genesis = lambda block: repr(block) == repr(self.blocks[0])
    if not is_valid_genesis(new_chain[0]):
      print('invalid genesis block')
      return False
    for i in range(1, len(new_chain)):
      if not self.is_valid_new_block(new_chain[i], new_chain[i-1]):
        print('block ' + i + ' in new chain is not valid')
        return False
    return True

  def replace_chain(self, new_blocks):
    if self.is_valid_chain(new_blocks) and len(new_blocks) > len(self.blocks):
      print('Received blockchain is valid. Replacing current blockchain with received chain.')
      self.blocks = new_blocks
    else:
      print('Received blockchain is invalid')

  