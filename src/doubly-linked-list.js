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
    this.prev.next = this.next.prev;
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
      const node = new ListNode(value, null, null);
      this.head = node;
      this.tail = node;
    } else {
      const node = new ListNode(value, null, this.head);
      this.head.insertBefore(node);
      this.head = node;
    }
  }

  /* Remove the list's current head. The list's
  `head` pointer should point to the removed node's
  `next` node */
  removeFromHead() {
    if (!this.head) return null;

    else if (!this.tail) {
      this.head = null;
      return null;
    }

    else {
      const oldHead = this.head;
      this.head = this.head.next;
      return oldHead.value;
    }
  }

  /* Adds the given value as the new tail
  node of the list */
  addToTail(value) {
    if (!this.head) this.head = new ListNode(value, null, null);

    else if (!this.tail) {
      const node = new ListNode(value, this.head, null)
      this.head.insertAfter(node);
      this.tail = node;
    }

    else {
      const node = new ListNode(value, this.tail, null);
      this.tail.insertAfter(node);
      this.tail = node;
    }
  }

  /* Remove the list's current tail. The list's
  `tail` pointer should point to the removed node's
  `prev` node */
  removeFromTail() {
    let tailRemoved;

    if (!this.tail && !this.head) tailRemoved = null;

    else if (!this.tail && this.head) {
      tailRemoved = this.head.value;
      this.head = null;
    }

    else if (this.tail.prev === this.head) {
      tailRemoved = this.tail.value;
      this.head.next = null;
      this.tail = null;
    }

    else {
      tailRemoved = this.tail.value;
      this.tail = this.tail.prev;
    }

    return tailRemoved;
  }

  /* Move the given node to the front of the
  list. Update the list's `head` pointer
  accordingly */
  moveToFront(node) {
    // if (!node.next && !node.prev) this.head = node;

    if (!node.next) {
      node.prev.next = null;
    }

    node.next.prev = node.prev.next;
    
    node.insertAfter(this.head);
    node.insertBefore(null);
    
    this.head.prev = node;
    this.head = node;
  }

  /* Move the given node to the back of the
  list. Update the list's `tail` pointer 
  accordingly */
  moveToBack(node) {

  }

  /* Delete the given node from the list */
  delete(node) {
    if (!node.next) this.removeFromTail(node);
    if (!node.prev) this.addToHead(node.prev);
    else node.delete();
  }
}

module.exports = DoublyLinkedList;