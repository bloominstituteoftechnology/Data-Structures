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
    let currentVal = this.value;
    this.next = value;
    this.prev = currentVal;
    // return next;


  }

  /* Insert the given value as the this node's
  `prev` node */
  insertBefore(value) {
    // let prevVal = value;
    // prev = prevVal;
    // return this.prevVal;

    let currVal = this.value;
    this.prev = value;
    this.next = currVal;
  }

  /* Delete this node */
  delete() {
    this.next.prev = this.prev;
    this.prev.next = this.next;

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
    let newNode = new ListNode(value);
    if(this.head){
      this.head.prev = newNode;
      newNode.next = this.head;
    }
    else {
      this.tail = newNode;
    }
    this.head = newNode;
  }

  /* Remove the list's current head. The list's
  `head` pointer should point to the removed node's
  `next` node */
  removeFromHead() {
    let theHead = this.head,
    value = null;

    if(theHead) {
      value = this.head.value;
      if(this.head.next != null){
        let oldHead = this.head;
        this.head = oldHead.next;
        this.head.previous = null;
        oldHead = null;
      }
      else{
        this.head = null;
        this.tail = null;
      }
    }
    else{
      //
    }
    return value;

  }

  /* Adds the given value as the new tail
  node of the list */
  addToTail(value) {
    let newNode = new ListNode(value);

    if(this.tail) {
      this.tail.next = newNode;
      newNode.prev = this.tail;
    } 
    else {
      this.head = newNode;
    }
    this.tail = newNode;
  }

  /* Remove the list's current tail. The list's
  `tail` pointer should point to the removed node's
  `prev` node */
  removeFromTail() {
    let theTail = this.tail,
    value = null;

    if(theTail) {
      value = this.tail.value;
      if(this.tail.previous !== null){
        let oldTail = this.tail;
        this.tail = oldTail.prev;
        this.tail.next = null;
      } else {
        this.head = null;
        this.tail = null;
      }
    }
    else {
      //
    }
    return value;

  }

  /* Move the given node to the front of the
  list. Update the list's `head` pointer
  accordingly */
  moveToFront(node) {
    const value = node.value;
    if (node === this.tail){
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
    }
    else {
      node.delete();
    }
    this.addToTail(value);
  }

  /* Delete the given node from the list */
  delete(node) {
    const leftChildIndex = index * 2 + 1;
    const rightChildIndex = index * 2 + 2;

    let maxChild;

    if (this.storage[leftChildIndex]) {
      if (!this.storage[rightChildIndex]) {
        maxChild = leftChildIndex;
      } else if (this.storage[rightChildIndex]) {
        maxChild = this.storage[leftChildIndex] > this.storage[rightChildIndex] ? 
      }
    }

  }
}

module.exports = DoublyLinkedList;