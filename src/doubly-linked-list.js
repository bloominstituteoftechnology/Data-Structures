class ListNode {
  /* Do not modify the constructor */
  constructor(value, prev = null, next = null) {
    this.value = value;
    this.prev = prev;
    this.next = next;
  }

  /* Insert the given value as this node's `next` node */
  insertAfter(value) {
    // go to 52:15 to see a visual explanation in seasn cs8 data struc lec
    // this squeezing in a node between the two nodes we have initially. So picture Two nodes.
    const currentNextNode = this.next; // Intially, this is point at our second node 
    // this is changing which node we're pointing too. Which is obvz the new one we're inserting
    this.next = new ListNode(value, this, currentNextNode); // new 3RD node we're inserting 
    // Now we're changing the 2ND node's pointer to point to our new node that has just been inserted
    if (currentNextNode) { // since our new node's next is pointing to "CurrentNextNode" we will have bidrectional communication.
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
  delete() {// this.prev is an enitre node reference. Same goes for this.next
    if (this.prev) { // this.prev.next is replacing the previous node with 
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
    if (!this.head) return null;
    const currentHead = this.head;
    this.head = this.head.next;

    if (this.head) {
      this.head.prev = null; // head can't have a previous
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
      this.tail.next = newNode;
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

    if (this.tail) {
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
    node.delete();
  }
}

module.exports = DoublyLinkedList;