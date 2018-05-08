class ListNode {
  /* Do not modify the constructor */
  constructor(value, prev = null, next = null) {
    this.value = value;
    this.prev = prev;
    this.next = next;
  }

  /* Insert the given value as this node's `next` node */
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
    // if this.head exist- point the new node to the prev 
    if (this.head) {
      this.head.prev = newNode;
    }
    // if there is no tail the tail is now the newNode we're inserting
    if (!this.tail) {
      this.tail = newNode;
    }
    this.head = newNode;
  }

  /* Remove the list's current head. The list's
  `head` pointer should point to the removed node's
  `next` node */
  removeFromHead() {
    if (!this.head) {
      return null;
    }
    const currentHead = this.head;
    this.head = this.head.next;

    if (this.head) {
      this.head.prev = null;
    }
    return currentHead.value;
  }

  /* Adds the given value as the new tail
  node of the list */
  addToTail(value) {
    const newNode = new ListNode(value, this.tail, null);
    if (!this.head) {
      this.head = newNode;
    }
    if (this.tail) {
      this.tail.next = null;
    }
    
    this.tail = newNode;
  }

  /* Remove the list's current tail. The list's
  `tail` pointer should point to the removed node's
  `prev` node */
  removeFromTail() {
    if (!this.tail) return null;
    
    const currentTail = this.tail;
    this.tail = this.tail.prev;

    if (this.tail)this.tail.next = null;
    
    return currentTail.value;
  }

  /* Move the given node to the front of the
  list. Update the list's `head` pointer
  accordingly */
  moveToFront(node) {
    const value = node.value;
    if (node === this.tail) {
      this.removeFromTail();
    } else {
      node.delete();
    }
    this.addToHead(value);
  }

  /* Move the given node to the back of the
  list. Update the list's `tail` pointer 
  accordingly */
  moveToBack(node) {
    const value = node.value;
    if (node === this.head) {
      this.removeFromHead();
    } else {
      node.delete();
    }
    this.addToTail(value);
  }

  /* Delete the given node from the list */
  delete(node) {
    node.delete();
  }
}

module.exports = DoublyLinkedList;