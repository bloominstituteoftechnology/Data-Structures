class LinkedList {
  /* Do not modify the constructor */
  constructor () {
    this.head = null
    this.tail = null
  }

  /* Add the given value to the tail
  of the list. The `tail` pointer
  should be updated accordingly */
  addToTail (value) {
    const newNode = {
      value: value,
      next: null
    } // Create a new node
    if (!this.head) {
      // check if the head is null, this means the node we are adding is the only element, we see the head and the tail to this new element
      this.head = newNode
      this.tail = newNode
      return
    }
    // if it is not, the tail.next will be set to the newNode and the elements before the newNode will be directed to the newNode this.tail=newNode
    this.tail.next = newNode
    this.tail = newNode
  }

  /* Remove the list's `head` value
  The `head` pointer should be updated
  accordingly */
  removeHead () {
    if (this.length === 0) {
      return undefined
    }
    const value = this.head.value
    this.head = this.head.next
    this.length--
    return value
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains (value) {
    let result = this.head
    while (result) {
      if (result.value === value) {
        return result
      }
      result = result.next
    }
    return result
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax () {}
}

module.exports = LinkedList
