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
    if (this.next) this.next.prev = value;
    value.next = this.next;
    this.next = value;
  }

  /* Insert the given value as the this node's
  `prev` node */
  insertBefore(value) {
    if (this.prev) this.prev.next = value;
    value.prev = this.prev;
    this.prev = value;
  }

  /* Delete this node */
  delete() {
    if (this.prev) this.prev.next = this.next;
    if (this.next) this.next.prev = this.prev;
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
    if (!this.head) {
      const newNode = new ListNode(value);
      this.head = newNode;
      this.tail = newNode;
    } else {
      let newNode = new ListNode(value, null, this.head);
      if (!this.tail) this.tail = newNode;
      this.head.insertBefore(newNode);
      this.head = newNode;
    }
  }

  /* Adds the given value as the new tail
  node of the list */
  addToTail(value) {
    if (!this.tail) {
      let newNode = new ListNode(value);
      this.tail = newNode;
      this.head = newNode;
    } else {
      let newNode = new ListNode(value, this.tail, null);
      if (!this.head) this.head = newNode;
      this.tail.insertAfter(newNode);
      this.tail = newNode;
    }
  }

  /* Remove the list's current head. The list's
  `head` pointer should point to the removed node's
  `next` node */
  removeFromHead() {
    if (!this.head) return null;
    const retVal = this.head.value;
    if (this.head.next) {
      this.head = this.head.next;
    } else {
      this.head.delete();
      this.head = null;
    }
    return retVal;
  }

  /* Remove the list's current tail. The list's
  `tail` pointer should point to the removed node's
  `prev` node */
  removeFromTail() {
    if (!this.tail) return null;
    const retVal = this.tail.value;
    if (this.tail.prev) this.tail = this.tail.prev;
    else {
      this.tail.delete();
      this.tail = null;
    }
    return retVal;
  }

  /* Move the given node to the front of the
  list. Update the list's `head` pointer
  accordingly */
  moveToFront(node) {
    if (node === this.tail) this.removeFromTail();
    if (node === this.head) this.removeFromHead();
    node.delete();
    this.addToHead(node.value);
  }

  /* Move the given node to the back of the
  list. Update the list's `tail` pointer 
  accordingly */
  moveToBack(node) {
    if (node === this.tail) this.removeFromTail();
    if (node === this.head) this.removeFromHead();
    node.delete();
    this.addToTail(node.value);
  }

  /* Delete the given node from the list */
  delete(node) {
    node.delete();
  }
}

module.exports = DoublyLinkedList;
