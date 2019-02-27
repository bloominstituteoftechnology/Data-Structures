class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if not self.value:
      self.value=value
    else:
      pointer= self
      finished=False
      while not finished:
        if value>pointer.value:
          if pointer.right:
            pointer=pointer.right
          else:
            pointer.right= BinarySearchTree(value)
            finished=True
        elif value< pointer.value:
          if pointer.left:
            pointer=pointer.left
          else: 
            pointer.left= BinarySearchTree(value)
            finished=True

  def contains(self, target):
    contains=False
    finshed=False
    pointer=self
    while not finshed:
      if pointer:
        if target==pointer.value:
          contains=True
          finshed=True
        elif target> pointer.value:
          pointer=pointer.right
        elif target< pointer.value:
          pointer=pointer.left
      else:
        finshed=True
    return contains

      

  def get_max(self):
    pointer=self
    max=None
    while pointer:
      max=pointer.value
      pointer=pointer.right
    return max
