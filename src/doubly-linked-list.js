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
  }

  /* Adds the given value as the new head
  node of the list */
  addToHead(value) {
    if(this.head !== null && this.tail !== null) {
      this.head.insertBefore(value);
      this.head = this.head.prev;
    } else {
      this.head = new ListNode(value);
      this.tail = this.head;
    }
  }

  /* Remove the list's current head. The list's
  `head` pointer should point to the removed node's
  `next` node */
  removeFromHead() {
    if(!this.head) return null;
    let value = this.head.value;
    this.head = this.head.next;
    if(this.head) this.head.prev = null;
    else this.tail = null;
    return value;
  }

  /* Adds the given value as the new tail
  node of the list */
  addToTail(value) {
    if(this.head !== null && this.tail !== null) {
      this.tail.insertAfter(value);
      this.tail = this.tail.next;
    } else {
      this.tail = new ListNode(value);
      this.head = this.tail;      
    }
  }

  /* Remove the list's current tail. The list's
  `tail` pointer should point to the removed node's
  `prev` node */
  removeFromTail() {
    if(!this.tail) return null;
    let value = this.tail.value;
    this.tail = this.tail.prev;
    if(this.tail) this.tail.next = null;
    else this.head = null;
    return value;
  }

  /* Move the given node to the front of the
  list. Update the list's `head` pointer
  accordingly */
  moveToFront(node) {
 let value = node.value;
 if(node === this.tail) {
   this.removeFromTail();
 } else node.delete();
 this.addToHead(value);
  }

  /* Move the given node to the back of the
  list. Update the list's `tail` pointer 
  accordingly */
  moveToBack(node) {
    let value = node.value;
    if(node === this.head) {
      this.removeFromHead();
    } else node.delete();
    this.addToTail(value);
  }

  /* Delete the given node from the list */
  delete(node) {
   node.next.prev = node.prev;
   node.prev.next = node.next;
  }
}

module.exports = DoublyLinkedList;