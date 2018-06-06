class LinkedList {
  /* Do not modify the constructor */
  constructor() {
    this.head = null;
    this.tail = null;
  }

  /* Add the given value to the tail
  of the list. The `tail` pointer
  should be updated accordingly */
  addToTail(value) {
    const node = { value: value, next: null }
    if (this.head == null) {
      this.head = node
    } else if (this.tail != null){
      this.tail.next = node
    }
    this.tail = node
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
    const node = this.head
    this.head = this.head.next
    return node.value
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let currentNode = this.head
    while (currentNode) {
      if (currentNode.value == value) {
        return true
      }
      currentNode = currentNode.next
    }
    return false
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    if (!this.head) return null
    
    let currentNode = this.head
    let max = currentNode.value
    while (currentNode) {
      if (currentNode.value > max) {
        max = currentNode.value
      }
      currentNode = currentNode.next
    }
    return max
  }
}

module.exports = LinkedList;