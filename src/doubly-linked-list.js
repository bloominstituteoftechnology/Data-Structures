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

  }

  /* Insert the given value as the this node's
  `prev` node */
  insertBefore(value) {

  }

  /* Delete this node */
  delete() {

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
    if (!this.head) {
      this.head = new ListNode(value) 
      this.tail = this.head;
      return;
    }
    let current = new ListNode(value, null, this.head); 
    this.head.prev = current;
    this.head = current;
  }

  /* Remove the list's current head. The list's
  `head` pointer should point to the removed node's
  `next` node */
  removeFromHead() {
    if (!this.head) return null;
    const store = this.head.value;
    this.head = this.head.next;
    if (this.head) {
      this.head.prev = null;
    }
    return store;
  }

  /* Adds the given value as the new tail
  node of the list */
  addToTail(value) {
    if (!this.head) {
      this.head = new ListNode(value);
      this.tail = this.head;
    } else {
      this.tail.next = new ListNode(value, this.tail);
      this.tail = this.tail.next;
    }
  }

  /* Remove the list's current tail. The list's
  `tail` pointer should point to the removed node's
  `prev` node */
  removeFromTail() {
    if (!this.head) return null;
    const store = this.tail.value;
    if (this.head === this.tail) {
      this.head = null;
      this.tail = null;
      return store;
    }
    this.tail = this.tail.prev;
    this.tail.next = null;
    return store;
  }

  /* Move the given node to the front of the
  list. Update the list's `head` pointer
  accordingly */
  moveToFront(node) {
    if (node.prev && node.next) {
      node.next.prev = node.prev;
      node.prev.next = node.next;
    } else if (node.prev) {
      node.prev.next = null;
      this.tail = node.prev;
    } else {
      return;
    }
    this.addToHead(node.value)
  }

  /* Move the given node to the back of the
  list. Update the list's `tail` pointer 
  accordingly */
  moveToBack(node) {
    if (node.prev && node.next) {
      node.next.prev = node.prev;
      node.prev.next = node.next;
    } else if (node.prev) {
      node.prev.next = null;
      this.tail = node.prev;
    } else if (node.next) {
      node.next.prev = null;
      this.head = node.next;
    }
    this.addToTail(node.value)
  }

  /* Delete the given node from the list */
  delete(node) {
    if (node.prev && node.next) {
      node.next.prev = node.prev;
      node.prev.next = node.next;
    } else if (node.prev) {
      node.prev.next = null;
      this.tail = node.prev;
    } else {
      return;
    }
  }
}

module.exports = DoublyLinkedList;