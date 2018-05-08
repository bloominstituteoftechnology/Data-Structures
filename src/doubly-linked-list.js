class ListNode {
  /* Do not modify the constructor 🙄 */
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
    this.next.prev = this.prev
    this.prev.next = this.next
  }
}

class DoublyLinkedList {
  /* Do not modify the constructor */
  constructor() {
    this.head = null
    this.tail = null
  }

  /* Adds the given value as the new head
  node of the list */
  addToHead(value) {
    const node = new ListNode(value)
    if (this.head) {
      this.head.prev = node
      node.next = this.head
      this.head = node
    } else {
      this.head = node
      this.tail = node
    }
  }

  /* Remove the list's current head. The list's
  `head` pointer should point to the removed node's
  `next` node */
  removeFromHead() {
    if (!this.head) return null

    const { value } = this.head
    if (this.head === this.tail) {
      this.head = null
      this.tail = null
    } else {
      this.head = this.head.next
      this.head.prev = null
    }
    return value
  }

  /* Adds the given value as the new tail
  node of the list */
  addToTail(value) {
    const node = new ListNode(value)
    if (this.head) {
      this.tail.next = node
      node.prev = this.tail
      this.tail = node
    } else {
      this.head = node
      this.tail = node
    }
  }

  /* Remove the list's current tail. The list's
  `tail` pointer should point to the removed node's
  `prev` node */
  removeFromTail() {
    if (!this.tail) return null

    const { value } = this.tail
    if (this.tail === this.head) {
      this.head = null
      this.tail = null
    } else {
      this.tail = this.tail.prev
      this.tail.next = null
    }
    return value
  }

  /* Move the given node to the front of the
  list. Update the list's `head` pointer
  accordingly */
  moveToFront(node) {
    node.next
      ? node.next.prev = node.prev
      : this.tail = node.prev

    node.prev.next = node.next
    node.prev = null
    node.next = this.head
    this.head.prev = node
    this.head = node
  }

  /* Move the given node to the back of the
  list. Update the list's `tail` pointer 
  accordingly */
  moveToBack(node) {
    let { head } = this
    while (head) {
      if (!head.next) {
        head.next = node
        break
      }
      head = head.next
    }

    node.prev
      ? node.prev.next = node.next
      : this.head = node.next

    node.next.prev = node.prev
    node.next = null
    node.prev = this.tail

    this.tail = node
  }

  /* Delete the given node from the list */
  delete(node) {
    node.delete()
  }
}

// const CircularJSON = require('circular-json')
// const list = new DoublyLinkedList()

// list.addToTail(2) // 2
// list.addToTail(3) // 2 -> 3
// list.addToHead(1) // 1 -> 2 -> 3
// console.log(CircularJSON.stringify(list, null, '\t')) // 1 -> 2 -> 3
// list.moveToFront(list.tail)
// console.log(CircularJSON.stringify(list, null, '\t')) // 3 -> 1 -> 2
// list.moveToFront(list.tail)
// console.log(CircularJSON.stringify(list, null, '\t')) // 2 -> 3 -> 1
// list.moveToBack(list.head)
// console.log(CircularJSON.stringify(list, null, '\t')) // 3 -> 1 -> 2
// list.moveToBack(list.head)
// console.log(CircularJSON.stringify(list, null, '\t')) // 1 -> 2 -> 3
// list.moveToFront(list.head.next)
// console.log(CircularJSON.stringify(list, null, '\t')) // 2 -> 1 -> 3
// list.moveToFront(list.tail)
// list.removeFromHead()
// list.removeFromHead()
// list.removeFromTail()

module.exports = DoublyLinkedList
