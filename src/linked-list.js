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
    const node = { value, next: null }

    if (!this.head) {
      this.head = node
      this.tail = node
      return
    }

    this.tail.next = node
    this.tail = node
  }

  /* Remove the list's `head` value
  The `head` pointer should be updated
  accordingly */
  removeHead() {
    const removed = this.head
    this.head = this.head.next
    return removed.value
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let tmp = this.head
    while (tmp) {
      if (tmp.value === value) return true
      tmp = tmp.next
    }
    return false
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    if (!this.head) return null
    let maximal = this.head.value
    let tmp = this.head
    while (tmp) {
      if (maximal < tmp.value) maximal = tmp.value
      tmp = tmp.next
    }
    return maximal
  }
}

module.exports = LinkedList