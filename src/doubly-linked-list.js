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
    const next = this.next;
    const newNode = {
      value: value,
      prev: this,
      next: next
    }
    next.prev = newNode;
    this.next = newNode;
  }

  /* Insert the given value as the this node's
  `prev` node */
  insertBefore(value) {
    const prev = this.prev;
    const newNode = {
      value: value,
      prev: prev,
      next: this
    }
    prev.next = newNode;
    this.prev = newNode;
  }

  /* Delete this node */
  delete() {
    const prev = this.prev;
    const next = this.next;
    prev.next = this.next;
    next.prev = this.prev;
    return this.value;
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
    const node = new ListNode(value, this.tail, this.head);
    if (this.head === null) this.head = node;
    else this.head.prev = node;
    if (this.tail === null) this.tail = node;
    else this.tail.next = node;
    this.head = node;
  }

  /* Remove the list's current head. The list's
  `head` pointer should point to the removed node's
  `next` node */
  removeFromHead() {
    this.head.prev.next = this.head.prev;
    this.head.next.prev = this.head.prev;
    return this.head.delete();
  }

  /* Adds the given value as the new tail
  node of the list */
  addToTail(value) {
    const node = new ListNode(value, this.tail, this.head);
    if(this.head === null) this.head = node;
    else this.head.prev = node;
    if (this.tail === null) this.tail = node;
    else this.tail.next = node;
    this.tail = node;
  }

  /* Remove the list's current tail. The list's
  `tail` pointer should point to the removed node's
  `prev` node */
  removeFromTail() {
    this.tail.prev.next = this.tail.next;
    this.tail.next.prev = this.tail.prev;
    return this.tail.delete();
  }

  /* Move the given node to the front of the
  list. Update the list's `head` pointer
  accordingly */
  moveToFront(node) {
    const newNode = node;
    newNode.next.prev = newNode.prev;
    newNode.prev.next = newNode.next;
    this.head.next.prev = newNode;
    this.tail.next = newNode;
    this.head = newNode;
    node.delete();
  }

  /* Move the given node to the back of the
  list. Update the list's `tail` pointer 
  accordingly */
  moveToBack(node) {
    const newNode = node;
    newNode.next.prev = newNode.prev;
    newNode.prev.next = newNode.next;
    this.head.prev = newNode;
    this.tail.prev.next = newNode;
    this.tail = newNode;
    node.delete();
  }

  /* Delete the given node from the list */
  delete(node) {
    node.delete();
  }
}

module.exports = DoublyLinkedList;