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
    let current = this.value; //value of current node we're on
    this.next = value; //value we want to pass in as next
    this.prev = current;
  }

  /* Insert the given value as the this node's
  `prev` node */
  insertBefore(value) {
    let current = this.value;
    this.prev = value;
    this.next = current;
  }

  /* Delete this node */
  delete() {
    this.next.prev = this.prev;
    this.prev.next = this.next;
  }

  // delete() {
  //   if (this.head === this.tail) {
  //     this.head = null;
  //     this.tail = null;
  //   } else {
  //     this.next.prev = this.prev;
  //     this.prev.next = this.next;
  //   }
  // }
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
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
      return;
    }
    this.head.prev = newNode;
    newNode.next = this.head;
    this.head = newNode;
  }

  /* Remove the list's current head. The list's
  `head` pointer should point to the removed node's
  `next` node */
  removeFromHead() {
    if (!this.head) {
      // no elements
      return null;
    }
    let valToRemove = this.head.value;
    if (this.head.next) {
      let newHead = this.head.next;
      newHead.prev = null;
      this.head = newHead;
    } else {
      // if theres one element, remove it
      this.tail = null;
      this.head = null;
    }
    return valToRemove;
  }

  /* Adds the given value as the new tail
  node of the list */
  addToTail(value) {
    const newNode = new ListNode(value);
    if (!this.head) {
      this.head = newNode;
      // this.tail = newNode;
      this.tail = this.head;
      return;
    }
    newNode.prev = this.tail;
    this.tail.next = newNode;
    this.tail = newNode;
  }

  /* Remove the list's current tail. The list's
  `tail` pointer should point to the removed node's
  `prev` node */
  removeFromTail() {
    if (this.tail !== null) {
      const removed = this.tail.value;
      this.tail = this.tail.prev;
      return removed;
    }
    return null;
  }

  // removeFromTail() {
  //   if (this.tail !== null) {
  //     const tailVal = this.tail.value;
  //     this.tail = this.tail.prev;
  //     return tailVal;
  //   } else {
  //     return null;
  //   }
  // }

  /* Move the given node to the front of the
  list. Update the list's `head` pointer
  accordingly */
  moveToFront(node) {
    this.head = this.head.next;
    node = this.head;
  }

  /* Move the given node to the back of the
  list. Update the list's `tail` pointer 
  accordingly */
  moveToBack(node) {
    this.tail = this.tail.prev;
    node = this.tail;
  }

  /* Delete the given node from the list */
  delete(node) {
    node.next.prev = this.prev;
    node.prev.next = this.next;
  }
}

const list = new DoublyLinkedList();
list.addToHead(3);
list.addToHead(39);
console.log(list.removeFromHead());
console.log(list.removeFromHead());

module.exports = DoublyLinkedList;
