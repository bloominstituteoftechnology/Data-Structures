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
    this.prev.next = this.next;
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
    if (!this.head || !this.tail) {
      this.head = this.tail = new ListNode(value);
    } else {
      this.head.insertBefore(value);
      this.head = this.head.prev;
    }
  }

  /* Remove the list's current head. The list's
  `head` pointer should point to the removed node's
  `next` node */
  removeFromHead() {
    if (this.head) {
      let value = this.head.value;
      this.head = this.head.next;
      return value;
    } else {
      return null;
    }
  }

  /* Adds the given value as the new tail
  node of the list */
  addToTail(value) {
    if (!this.tail || !this.head) {
      this.head = this.tail = new ListNode(value);
    } else {
      this.tail.insertAfter(value);
      this.tail = this.tail.next;
    }
  }

  /* Remove the list's current tail. The list's
  `tail` pointer should point to the removed node's
  `prev` node */
  removeFromTail() {
    if (this.tail) {
      let value = this.tail.value;
      this.tail = this.tail.prev;
      return value;
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
    node.next.prev = node.prevl;
    node.next = null;
    node.prev = this.tail;
    this.tail = node;
  }

  /* Delete the given node from the list */
  delete(node) {
    node.prev.next = node.next;
    node.next.prev = node.prev;
  }
}

module.exports = DoublyLinkedList;
