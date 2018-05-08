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
    this.next = new ListNode(value, this, this.next);
  }

  /* Insert the given value as the this node's
  `prev` node */
  insertBefore(value) {
    this.prev = new ListNode(value, this.prev, this);
  }

  /* Delete this node */
  delete() {}
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
    const newNode = new ListNode(value)
    if (!this.head || !this.tail) {
      this.head = newNode;
      this.tail = newNode;
      return;
    }
    this.head.insertBefore(value);
    this.head = this.head.prev;
  }

  /* Remove the list's current head. The list's
  `head` pointer should point to the removed node's
  `next` node */
  removeFromHead() {
    if (!this.head) return null;
    let currentHead = this.head;
    this.head = this.head.next;
    if (this.head) this.head.prev = null;
    else this.tail = null;
    return currentHead.value;
  }

  /* Adds the given value as the new tail
  node of the list */
  addToTail(value) {
    const newNode = new ListNode(value)
    if (!this.head || !this.tail) {
      this.head = newNode;
      this.tail = newNode;
      return;
    }
    this.tail.insertAfter(value);
    this.tail = this.tail.next;
  }

  /* Remove the list's current tail. The list's
  `tail` pointer should point to the removed node's
  `prev` node */
  removeFromTail() {
    if (!this.tail) return null;
    let currentTail = this.tail;
    this.tail = this.tail.prev;
    if (this.tail) this.tail.next = null;
    else this.tail = null;
    return currentTail.value;
  }

  /* Move the given node to the front of the
  list. Update the list's `head` pointer
  accordingly */
  moveToFront(node) {
    if (this.head === this.tail) return;
    this.addToHead(node.value);
    // console.log('\n\n\n---node:',node);
    node.prev.next = node.next;
    if (node.next)node.next.prev = node.prev;
    else this.tail = node.prev;
  }

  /* Move the given node to the back of the
  list. Update the list's `tail` pointer 
  accordingly */
  moveToBack(node) {
    if (this.head === this.tail) return;
    // this.head = node;
    // // console.log('\n\n\n---node:',node);
    // node.prev.next = node.next;
    // if (node.next) node.next.prev = node.prev
    // else return
    // console.log('\n\n\n---this.prev.next', node.prev.next);
    // console.log('\n\nn\---this.next.prev', node.next.prev);
    if (node === this.head ) this.head = node.next;
      if (node.prev) node.prev.insertAfter(node.next);
      if (node.next) node.next.insertBefore(node.prev);
      this.addToTail(node.value);
  }

  /* Delete the given node from the list */
  delete(node) {
    node.prev.next = node.next;
    node.next.prev = node.prev;
  }
}

module.exports = DoublyLinkedList;