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
    if (currentNextNode) {
      currentNextNode.prev = this.next;
    }
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
    // check if the head is null
    if (this.head) {
      this.head.prev = newNode;
    }

    // check if the tail is null, then set newNode to tail as well
    if (!this.tail) {
      this.tail = newNode;
    }

    // make the newNode the head
    this.head = newNode;
  }

  /* Remove the list's current head. The list's
  `head` pointer should point to the removed node's
  `next` node */
  removeFromHead() {
    // check if head is null
    if (!this.head) return null;

    // get copy of the the head
    const currentHead = this.head;
    // change the pointer from the current head, to the next item
    this.head = this.head.next;

    // do a check to make sure the head exists
    if (this.head) {
      // make the prev pointer null
      this.head.prev = null;
    }
    return currentHead.value;
  }

  /* Adds the given value as the new tail
  node of the list */
  addToTail(value) {
    const newNode = new ListNode(value, this.tail, null);

    // check if the head is null
    if (!this.head) {
      // set head to the newNode
      this.head = newNode;
    }

    // check if the tail exists
    if (this.tail) {
      this.tail.next = newNode;
    }

    // make the newNode the tail
    this.tail = newNode;
  }

  /* Remove the list's current tail. The list's
  `tail` pointer should point to the removed node's
  `prev` node */
  removeFromTail() {
    // check if head is null
    if (!this.tail) return null;
    // get copy of the the tail
    const currentTail = this.tail;

    // change the pointer from the current tail, to the next item
    this.tail = this.tail.prev;

    // do a check to make sure tail exists
    if (this.tail) {
      // make the next pointer null
      this.tail.next = null;
    }
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
    // remove the node from the linked list
    node.delete();
  }
}

module.exports = DoublyLinkedList;
