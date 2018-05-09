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
    const currentNextNode = this.next;
    this.next = new ListNode(value, this, currentNextNode);
    if (currentNextNode) currentNextNode.prev = this.next;
  }

  /* Insert the given value as the this node's
  `prev` node */
  insertBefore(value) {
    const currentPrevNode = this.prev;
    this.prev = new ListNode(value, currentPrevNode, this);
    if (currentPrevNode) {
      currentPrevNode.next = this.prev;
    }
  }

  /* Delete this node */
  delete() {
    if (this.prev) {
      this.prev.next = this.next;
    }
    if (this.next) {
      this.next.prev = this.prev;
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
    const newNode = new ListNode(value, null, this.head);
    if (this.head) {
      this.head.prev = newNode;
    }
    if (!this.tail) {
      this.tail = newNode;
    }
    this.head = newNode;
  }

  /* Remove the list's current head. The list's
  `head` pointer should point to the removed node's
  `next` node */
  removeFromHead() {
    if (!this.head) return null;
    const removedValue = this.head.value;
    this.head = this.head.next;
    if (this.head) this.head.prev = null;
    return removedValue;
  }

  /* Adds the given value as the new tail
  node of the list */
  addToTail(value) {
    const newNode = new ListNode(value, this.tail, null);
    if (!this.head) this.head = newNode;
    if (this.tail) this.tail.next = newNode;
    this.tail = newNode;
  }

  /* Remove the list's current tail. The list's
  `tail` pointer should point to the removed node's
  `prev` node */
  removeFromTail() {
    if (!this.tail) return null;
    const removedValue = this.tail.value;
    this.tail = this.tail.prev;
    if (this.tail) this.tail.next = null;
    return removedValue;
  }

  /* Move the given node to the front of the
  list. Update the list's `head` pointer
  accordingly */
  moveToFront(node) {
    const value = node.value;
    node === this.tail ? this.removeFromTail() : node.delete();
    this.addToHead(value);
  }

  /* Move the given node to the back of the
  list. Update the list's `tail` pointer 
  accordingly */
  moveToBack(node) {
    const value = node.value;
    node === this.head ? this.removeFromHead() : node.delete();
    this.addToTail(value);
  }

  /* Delete the given node from the list */
  delete(node) {
    node.delete();
  }
}

module.exports = DoublyLinkedList;
