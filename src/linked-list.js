class LinkedList {
  /* Do not modify the constructor */
  constructor() {
    this.head = null
    this.tail = null
  }

  /* Add the given value to the tail
  of the list. The `tail` pointer
  should be updated accordingly */
  addToTail(value) {
    const newNode = {
      value: value,
      next: null
    }

    if (!this.head) {
      this.head = newNode
      this.tail = newNode
    } else {
      let currentNode = this.head
      while (currentNode.next) {
        currentNode = currentNode.next
      }
      currentNode.next = newNode
      this.tail = newNode
    }
    this.length++ //?
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
    let headValue = null
    if (!this.head) {
      return headValue
    } else {
      headValue = this.head.value
      this.head = this.head.next
    }
    return headValue
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    if (this.head.value === value) return true
    let currentNode = this.head
    while (currentNode.next) {
      if (currentNode.next.value === value) return true
      currentNode = currentNode.next
    }
    return false
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    if (!this.head) return null
    let max = this.head.value
    let currentNode = this.head
    while (currentNode.next) {
      if (currentNode.next.value > max) max = currentNode.next.value
      currentNode = currentNode.next
    }
    return max
  }
}

module.exports = LinkedList
