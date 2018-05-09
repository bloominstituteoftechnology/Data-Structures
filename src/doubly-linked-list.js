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
    const newNode = new ListNode(value, this);
    this.next = newNode;

  }

  /* Insert the given value as the this node's
  `prev` node */
  insertBefore(value) {
    const newNode = new ListNode(value, this.prev, this);
    this.prev = newNode;

  }

  /* Delete this node */
  delete() {
    if (this.prev)
      this.prev.next = this.next;

    if (this.next)
      this.next.prev = this.prev;
  }

  print()
    {
      if (this.prev)
        console.log('Prev:', this.prev.value);
      else
        console.log('prev: null');

      console.log('value:', this.value);

      if (this.next)
        console.log('next:', this.next.value)
      else
        console.log('next: null');
    }
}

class DoublyLinkedList {
  /* Do not modify the constructor */
  constructor() {
    this.head = null;
    this.tail = null;
  }

  printList() {
    console.log('head:', this.head.value);
    let i = this.head;
    while (i) {
      i.print();
      i = i.next;
    }
    console.log('tail:', this.tail.value);
  }
  /* Adds the given value as the new head
  node of the list */
  addToHead(value) {
    if (!this.head) {
      const newNode = new ListNode(value);
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.head.insertBefore(value);
      this.head = this.head.prev;
    }

    
    

  }

  /* Remove the list's current head. The list's
  `head` pointer should point to the removed node's
  `next` node */
  removeFromHead() {
    if (!this.head)
      return null;
    let value;
    if (!this.head.next) {
      value = this.head.value
      this.head = null;
      this.tail = null;
      return value;
    }

    value = this.head.value;
    this.head = this.head.next;
    return value;
    
  }

  /* Adds the given value as the new tail
  node of the list */
  addToTail(value) {
    if (!this.tail){
      const newNode = new ListNode(value);
      this.tail = newNode;
      this.head = newNode;
    } else {
      const newNode = new ListNode(value, this.tail, null);
      this.tail.next = newNode;
      this.tail = newNode;
    }

  }

  /* Remove the list's current tail. The list's
  `tail` pointer should point to the removed node's
  `prev` node */
  removeFromTail() {
    if (!this.tail)
      return null;
    let value;
    if (!this.tail.prev) {
      value = this.tail.value;
      this.tail = null;
      this.head = null;
      return value;
    }

    value = this.tail.value;
    this.tail = this.tail.prev;
    this.tail.next = null;
    return value;

  }

  /* Move the given node to the front of the
  list. Update the list's `head` pointer
  accordingly */
  moveToFront(node) {

    if (node === this.head)
      return;
    
    if (node === this.tail) {
      this.tail = this.tail.prev;
      this.tail.next = null;
      node.next = this.head;
      node.prev = null;
      this.head = node;
      return;
    }

    node.prev.next = node.next;
    node.next.prev = node.prev;
    node.prev = null;
    node.next = this.head;
    this.head.prev = node;
    this.head = node;
    
  }

  /* Move the given node to the back of the
  list. Update the list's `tail` pointer 
  accordingly */
  moveToBack(node) {
    if (node === this.tail)
      return;
    
    if (node === this.head) {
      this.head = this.head.next;
      this.head.prev = null;
      this.tail.next = node;
      node.prev = this.tail;
      this.tail = node;
      node.next = null;
      return;
    }

    node.prev.next = node.next;
    node.next.prev = node.prev;
    node.prev = this.tail;
    this.tail.next = node;
    node.next = null;
    this.tail = node;

  }

  /* Delete the given node from the list */
  delete(node) {
    if (this.tail === this.head && node === this.head) {
      this.head = null;
      this.tail = null;
      return;
    }
    
    if (node === this.head) {
      this.head = this.head.next;
      this.head.prev = null;
      return;
    }

    if (node === this.tail) {
      this.tail = this.tail.prev;
      this.tail.next = null;
      return;
    }

    node.delete();
  }
}

module.exports = DoublyLinkedList;