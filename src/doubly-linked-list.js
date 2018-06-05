class ListNode {
  /* Do not modify the constructor */
  constructor(value, prev = null, next = null) {
    this.value = value;
    this.prev = prev;
    this.next = next;
  }

  /* Insert the given value as this node's
  `next` node */
  insertAfter(value) {
    const node = new ListNode(value, this)
    if (this.next) {
      node.next = this.next
    }
    this.next = node
  }

  /* Insert the given value as the this node's
  `prev` node */
  insertBefore(value) {
    const node = new ListNode(value, null, this)
    if (this.prev) {
      node.prev = this.prev
    }
    this.prev = node
  }

  /* Delete this node */
  delete() {
    [this.prev.next, this.next.prev] = [this.next, this.prev]
  }
}

class DoublyLinkedList {
  /* Do not modify the constructor */
  constructor() {
    this.head = null;
    this.tail = null;
  }

  /* Adds the given value as the new head
  node of the list */
  addToHead(value) {
    if (this.head) {
      this.head.insertBefore(value)
      this.head = this.head.prev
    } else {
      this.head = new ListNode(value)
    }

    if (!this.tail) {
      this.tail = this.head
    }
  }

  /* Remove the list's current head. The list's
  `head` pointer should point to the removed node's
  `next` node */
  removeFromHead() {
    if (!this.head) {
      return null
    }
    const value = this.head.value
    this.head = this.head.next
    if (this.head) {
      this.head.prev = null
    }
    return value
  }

  /* Adds the given value as the new tail
  node of the list */
  addToTail(value) {
    if (!this.head) {
      this.head = new ListNode(value)
      this.tail = this.head
    } else if (this.tail) {
      this.tail.insertAfter(value)
      this.tail = this.tail.next
    }
  }

  /* Remove the list's current tail. The list's
  `tail` pointer should point to the removed node's
  `prev` node */
  removeFromTail() {
    if (!this.tail) {
      return null
    }
    const value = this.tail.value
    this.tail = this.tail.prev
    return value
  }

  /* Move the given node to the front of the
  list. Update the list's `head` pointer
  accordingly */
  moveToFront(node) {
    if (this.tail === node && node.prev) {
      this.tail = node.prev
    }
    while (node.prev != null) {
      node.prev.next = node.next
      node.next = node.prev
      node.prev = node.prev.prev
    }
    this.head = node
  }

  /* Move the given node to the back of the
  list. Update the list's `tail` pointer 
  accordingly */
  moveToBack(node) {
    if (this.head === node && node.next) {
      this.head = node.next
    }
    while (node.next != null) {
      node.next.prev = node.prev
      node.prev = node.next
      node.next = node.next.next
    }
    this.tail = node
  }

  /* Delete the given node from the list */
  delete(node) {
    if (this.tail === node) {
      this.tail = node.prev
    }
    if (this.head === node) {
      this.head = node.next
    }
    node.prev.next = node.next
    node.next.prev = node.prev
  }
}

module.exports = DoublyLinkedList;