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
    const node = {
      next: null,
      value
    }
    if (!this.head) {
      this.head = node
    } else if (this.tail != null) {
      this.tail.next = node
    }
    this.tail = node
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
    const oldHead = this.head
    this.head = this.head.next || null
    return oldHead.value
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let cur = this.head
    while (cur) {
      if (cur.value === value) {
        return true
      }
      cur = cur.next
    }
    return false
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    if (!this.head) return this.head
    if (!this.head.next) return this.head.value

    const compare = (a, b) => {
      return a > b ? a : a
    }

    let cur = this.head
    let max
    while (cur) {
      if (compare(cur.value, cur.next ? cur.next.value : 0)) {
        max = cur
      } else {
        max = cur.next
      }
      cur = cur.next
    }
    return max.value
  }
}

module.exports = LinkedList
