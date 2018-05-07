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
    this.next = value
  }

  /* Insert the given value as the this node's
  `prev` node */
  insertBefore(value) {
    this.prev = value
  }

  /* Delete this node */
  delete() {
    this.prev = null
    this.next = null
  }
}

class DoublyLinkedList {
  /* Do not modify the constructor */
  constructor() {
    this.size = 0
    this.head = null
    this.tail = null
  }

  /* Adds the given value as the new head
  node of the list */
  addToHead(value) {
    const node = new ListNode(value)
    if (!this.head) {
      this.head = node
      this.tail = this.head
      // this.size++
      return
    }
    node.next = this.head
    this.head = node
    this.head.next.prev = this.head
  }

  /* Remove the list's current head. The list's
  `head` pointer should point to the removed node's
  `next` node */
  removeFromHead() {
    if (!this.head) return null
    const removed = this.head.value
    this.head = this.head.next
    return removed
  }

  /* Adds the given value as the new tail
  node of the list */
  addToTail(value) {
    const node = new ListNode(value)
    if (!this.head) {
      this.head = node
      this.tail = node
      this.size++
      return
    }
    this.tail.next = node
    node.prev = this.tail
    this.tail = node
    this.size++
  }

  /* Remove the list's current tail. The list's
  `tail` pointer should point to the removed node's
  `prev` node */
  removeFromTail() {
    let tmp = this.head
    while (tmp) {
      if (!tmp.next.next) {
        const removed = tmp.next.value
        tmp.next = null
        this.tail = tmp
        return removed
      }
      tmp = tmp.next
    }
  }

  /*
  {
    head: {
      value: 18,
      prev: null,
      next: {
        value: 109,
        prev: {
          value: 18
        },
        next: null
      }
    },
    tail: {
      value: 109
    }
  }

  */

  /* Move the given node to the front of the
  list. Update the list's `head` pointer
  accordingly */
  moveToFront(node) {}

  /* Move the given node to the back of the
  list. Update the list's `tail` pointer 
  accordingly */
  moveToBack(node) {}

  /* Delete the given node from the list */
  delete(node) {}
}

module.exports = DoublyLinkedList
