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
    const newNode = new ListNode(value);
    newNode.next = this.next;
    newNode.prev = this;
    this.next = newNode;
    newNode.next.prev = newNode;
  }

  /* Insert the given value as the this node's
  `prev` node */
  insertBefore(value) {
    const newNode = new ListNode(value);
    newNode.next = this;
    newNode.prev = this.prev;
    this.prev = newNode;
    newNode.prev.next = newNode;
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
    if (this.head !== null) {
      this.head.insertBefore(value);
    } else {
      this.head = new ListNode(value);
    }
    // const newNode = {
    //   value: value,
    //   next: null,
    // };
    // if (this.head === null) {
    //   this.head = newNode;
    //   this.tail = newNode;
    // } else {
    //   newNode.next = this.head;
    //   this.head.prev = newNode;
    //   this.head = newNode;
    // }
  }

  /* Remove the list's current head. The list's
  `head` pointer should point to the removed node's
  `next` node */
  removeFromHead() {
    if (this.head !== null) {
      this.head = this.head.next;
      this.head.prev = null;
    }
  }

  /* Adds the given value as the new tail
  node of the list */
  addToTail(value) {
    const newNode = {
      value: value,
      next: null,
    };
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
      return;
    }
    this.tail.next = newNode;
    this.tail = newNode;
  }

  /* Remove the list's current tail. The list's
  `tail` pointer should point to the removed node's
  `prev` node */
  removeFromTail() {
    if (this.tail !== null) {
      const currentTail = this.tail;
      this.tail = currentTail.prev;
      this.tail.next = null;
    }
  }

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

module.exports = DoublyLinkedList;
