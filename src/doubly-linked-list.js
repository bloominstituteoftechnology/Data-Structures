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

    this.next = value;
  }

  /* Insert the given value as the this node's
  `prev` node */
  insertBefore(value) {

    this.prev = value;
  }

  /* Delete this node */
  delete() {

    this.prev = null;
    this.next = null;
  }
}

class DoublyLinkedList {
  /* Do not modify the constructor */
  constructor() {
    this.head = null;
    this.tail = null;
    this.value = null;
  }

  /* Adds the given value as the new head
  node of the list */
  addToHead(value) {

    if (!this.head) {
      const newNode = new ListNode(value, null, null);
      this.head = newNode;
      this.tail = newNode;
    } else {
      const newNode = new ListNode(value, null, this.head);
      this.head.insertBefore(newNode);
      this.head = newNode;
    }
  }

  /* Remove the list's current head. The list's
  `head` pointer should point to the removed node's
  `next` node */
  removeFromHead() {

    if (!this.head) {
      return null;
    } else {
      const currentHead = this.head;
      this.head = currentHead.next;
      if (this.head) this.head.insertBefore(null);
      currentHead.delete();
      return currentHead.value;
    }
  }

  /* Adds the given value as the new tail
  node of the list */
  addToTail(value) {

    const newTail = new ListNode(value, this.tail, null);
    if (!this.head) {
      this.head = newTail;
      this.tail = newTail;
    } else {
    this.tail.insertAfter(newTail);
    this.tail = newTail;
    }
  }

  /* Remove the list's current tail. The list's
  `tail` pointer should point to the removed node's
  `prev` node */
  removeFromTail() {
    if (!this.tail) {
      return null;
    }
    if (!this.tail.prev) {
      const value = this.tail.value;
      this.tail = null;
      this.head = null;
      return value;
    }
      const currentTail = this.tail;
      this.tail = currentTail.prev;
      this.tail.insertAfter(null);
      currentTail.delete();
      return currentTail.value;
    }


  /* Move the given node to the front of the
  list. Update the list's `head` pointer
  accordingly */
  moveToFront(node) {

    if (node === this.tail) this.tail = node.prev;
    if (node.prev) node.prev.insertAfter(node.next);
    if (node.next) node.next.insertBefore(node.prev)
    this.addToHead(node.value);
  }

  /* Move the given node to the back of the
  list. Update the list's `tail` pointer 
  accordingly */
  moveToBack(node) {

      if (node === this.head ) this.head = node.next;
      if (node.prev) node.prev.insertAfter(node.next);
      if (node.next) node.next.insertBefore(node.prev);
      this.addToTail(node.value);
  }

  /* Delete the given node from the list */
  delete(node) {

    if (node === this.tail) this.tail = node.prev;
    if (node === this.head ) this.head = node.next;
    if (node.prev) node.prev.insertAfter(node.next);
    if (node.next) node.next.insertBefore(node.prev);
  }
}

module.exports = DoublyLinkedList;