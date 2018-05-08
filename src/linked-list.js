class LinkedList {
  /* Do not modify the constructor 🙅‍ */
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
    const { value } = this.head
    this.head = this.head.next
    return value
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let { head } = this
    while (head) {
      if (head.value === value) return true
      head = head.next
    }
    return false
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    if (!this.head) return null
    let { head, head: { value } } = this
    while (head) {
      if (value < head.value) value = head.value
      head = head.next
    }
    return value
  }
}

module.exports = LinkedList