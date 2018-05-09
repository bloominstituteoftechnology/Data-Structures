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
    this.next = new ListNode(value, this, this.next);
  }

  /* Insert the given value as the this node's
  `prev` node */
  insertBefore(value) {
    this.prev = new ListNode(value, this.prev, this);
  }

  /* Delete this node */
  delete() {
    if (this.head === this.tail) {
      this.head = null;
      this.tail = null;
    } else {
      this.next.prev = this.prev;
      this.prev.next = this.next;
    }
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
    if (this.head !== null && this.tail !== null) {
      this.head.insertBefore(value);
      this.head = this.head.prev;
    } else {
      this.head = new ListNode(value);
      this.tail = this.head;
    }
  }

  /* Remove the list's current head. The list's
  `head` pointer should point to the removed node's
  `next` node */
  removeFromHead() {
    if (this.head !== null) {
      const headVal = this.head.value;
      this.head = this.head.next;
      return headVal;
    } else {
      return null;
    }
  }

  /* Adds the given value as the new tail
  node of the list */
  addToTail(value) {
    if (this.head !== null && this.tail !== null) {
      this.tail.insertAfter(value);
      this.tail = this.tail.next;
    } else {
      this.head = new ListNode(value);
      this.tail = this.head;
    }
  }

  /* Remove the list's current tail. The list's
  `tail` pointer should point to the removed node's
  `prev` node */
  removeFromTail() {
    if (this.tail !== null) {
      const tailVal = this.tail.value;
      this.tail = this.tail.prev;
      return tailVal;
    } else {
      return null;
    }
  }

  /* Move the given node to the front of the
  list. Update the list's `head` pointer
  accordingly */
  moveToFront(node) {
    if (node.next) {
      node.next.prev = node.prev;
    } else {
      this.tail = node.prev;
    }
    node.prev.next = node.next;
    node.prev = null;
    node.next = this.head;
    this.head.prev = node;
    this.head = node;
  }

  /* Move the given node to the back of the
  list. Update the list's `tail` pointer 
  accordingly */
  moveToBack(node) {
    if (node.prev) {
      node.prev.next = node.next;
    } else {
      this.head = node.next;
    }
    node.next.prev = node.prev;
    node.next = null;
    node.prev = this.tail;
    this.tail.next = node;
    this.tail = node;
  }

  /* Delete the given node from the list */
  delete(node) {
    node.next.prev = node.prev;
    node.prev.next = node.next;
  }
}

module.exports = DoublyLinkedList;
