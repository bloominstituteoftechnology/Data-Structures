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
    // const newNode = {
    //   value: value,
    // };
  }

  /* Insert the given value as the this node's
  `prev` node */
  insertBefore(value) {
    // const newNode = new ListNode({
    //   value: value,
    //   next: this,
    //   prev: this.prev,
    // });
    // this.prev = newNode;
  }

  /* Delete this node */
  delete() {}
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
    const newNode = new ListNode(value);
    if (!this.head && !this.tail) {
      this.head = newNode;
      this.tail = newNode;
    }
    if (this.head === this.tail) {
      this.tail.prev = newNode;
      newNode.next = this.tail;
    }
    if (this.head) {
      this.head.prev = newNode;
      newNode.next = this.head;
    }
    this.head = newNode;
    console.log(this);
  }

  /* Remove the list's current head. The list's
  `head` pointer should point to the removed node's
  `next` node */
  removeFromHead() {
    if (!this.head) return null;
    const removedValue = this.head.value;
    this.head = this.head.next;
    // this.head.prev = null;
    return removedValue;
  }

  /* Adds the given value as the new tail
  node of the list */
  addToTail(value) {
    const newNode = new ListNode(value);
    if (!this.head) {
      this.head = newNode;
    }
    if (this.tail) {
      this.tail.next = newNode;
      newNode.prev = this.tail;
    }
    this.tail = newNode;
  }

  /* Remove the list's current tail. The list's
  `tail` pointer should point to the removed node's
  `prev` node */
  removeFromTail() {
    if (!this.tail) return null;
    const removedValue = this.tail.value;
    this.tail = this.tail.prev;
    return removedValue;
  }

  /* Move the given node to the front of the
  list. Update the list's `head` pointer
  accordingly */
  moveToFront(node) {
    if (node.prev) node.prev.next = node.next;
    node.next ? (node.next.prev = node.prev) : (this.tail = node.prev);
    this.addToHead(node.value, null, this.head);
  }

  /* Move the given node to the back of the
  list. Update the list's `tail` pointer 
  accordingly */
  moveToBack(node) {
    // console.log(JSON.stringify(node, null, 2), 'node');
    if (!node.next) return null;
    if (node.next) node.next.prev = node.prev;
    node.prev ? (node.prev.next = node.next) : (this.head = node.next);
    this.addToTail(node.value, this.tail, null);
    // console.log(JSON.stringify(this.head, null, 2), 'head');
  }

  /* Delete the given node from the list */
  delete(node) {
    const removedValue = node.value;
    node.prev = node.next;
    node.next = node.prev;
    return removedValue;
  }
}

module.exports = DoublyLinkedList;
