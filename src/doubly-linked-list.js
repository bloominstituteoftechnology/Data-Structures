class ListNode {
  /* Do not modify the constructor */
  constructor(value, prev = null, next = null) {
    this.value = value
    this.prev = prev
    this.next = next
  }

  /* Insert the given value as this node's
  `next` node */
  insertAfter(value) {
    const newNode = {
      value: value
    }
  }

  /* Insert the given value as the this node's
  `prev` node */
  insertBefore(value) {
    const newNode = new ListNode({
      value: value,
      next: this,
      prev: this.prev
    })
    this.prev = newNode
  }
  /* Delete this node */
  delete() {}
}

class DoublyLinkedList {
  /* Do not modify the constructor */
  constructor() {
    this.head = null
    this.tail = null
    this.length = 0
  }

  /* Adds the given value as the new head
  node of the list */
  addToHead(value) {
    if (this.length < 0) this.length = 0

    const newNode = new ListNode(value, null, this.head)

    if (this.length === 0) {
      this.head = newNode
      this.tail = newNode
      this.length++
    } else if (this.length === 1) {
      this.tail = this.head
      this.tail.prev = newNode
      this.head = newNode
      this.length++
    } else {
      this.head.prev = newNode
      this.head = newNode
      this.length++
    }
  }

  /* Remove the list's current head. The list's
  `head` pointer should point to the removed node's
  `next` node */
  removeFromHead() {
    let removed = null
    if (this.length < 0) this.length = 0
    if (this.length === 0) {
      this.head = null
      this.tail = null
      removed = null
      this.length--
    } else if (this.length === 1) {
      removed = this.head.value
      this.head = null
      this.tail = null
      this.length--
    } else {
      const newNode = {
        value: this.head.next.value,
        next: this.head.next.next,
        prev: null
      }
      removed = this.head.value
      this.head = newNode
      this.length--
    }
    return removed
  }

  /* Adds the given value as the new tail
  node of the list */
  addToTail(value) {
    if (this.length < 0) this.length = 0
    if (this.length === 0) {
      const newNode = {
        value: value,
        next: null,
        prev: null
      }
      this.head = newNode
      this.tail = newNode
      this.length++
    } else if (this.length === 1) {
      const newNode = {
        value: value,
        next: null,
        prev: this.head
      }
      this.head.next = newNode
      this.tail = newNode
      this.length++
    } else {
      const newNode = {
        value: value,
        next: null,
        prev: this.tail
      }
      this.tail.next = newNode
      this.tail = newNode
      this.length++
    }
  }

  /* Remove the list's current tail. The list's
  `tail` pointer should point to the removed node's
  `prev` node */
  removeFromTail() {
    if (this.length < 0) this.length = 0
    let removed = null
    if (this.length === 0) {
      this.head = null
      this.tail = null
      this.length--
    } else if (this.length === 1) {
      removed = this.head.value
      this.head = null
      this.tail = null
      this.length--
    } else if (this.length === 2) {
      removed = this.tail.value
      this.head.next = null
      this.tail = null
      this.length--
    } else {
      removed = this.tail.value
      this.tail.prev.next = null
      this.length--
    }
    return removed
  }

  /* Move the given node to the front of the
  list. Update the list's `head` pointer
  accordingly */
  moveToFront(node) {
    if (node.prev) node.prev.next = node.next
    node.next ? (node.next.prev = node.prev) : (this.tail = node.prev)
    this.addToHead(node.value, null, this.head)
  }

  /* Move the given node to the back of the
  list. Update the list's `tail` pointer
  accordingly */
  moveToBack(node) {
    if (node.next) node.next.prev = node.prev
    node.prev ? (node.prev.next = node.next) : (this.head = node.next)
    this.addToTail(node.value, this.tail, null)
  }

  /* Delete the given node from the list */
  delete(node) {
    node.prev ? (node.prev.next = node.next) : (this.head = node.next)
    node.next ? (node.next.prev = node.prev) : (this.tail = node.prev)
  }
}

module.exports = DoublyLinkedList
