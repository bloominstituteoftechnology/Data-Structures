// class ListNode {
//   /* Do not modify the constructor */
//   constructor(value, prev = null, next = null) {
//     this.value = value;
//     this.prev = prev;
//     this.next = next;
//   }

//   /* Insert the given value as this node's
//   `next` node */
//   insertAfter(value) {
//     const newNode = {
//       value: value,
//       prev: this,
//       next: this.next
//     }
//     this.next = newNode;
//   }

//   /* Insert the given value as the this node's
//   `prev` node */
//   insertBefore(value) {
//     const newNode = {
//       value: value,
//       prev: this.prev,
//       next: this
//     }
//     this.next = newNode;
//   }

//   /* Delete this node */
//   delete() {

//   }
// }

class DoublyLinkedList {
  /* Do not modify the constructor */
  constructor() {
    this.head = null;
    this.tail = null;
  }

  /* Adds the given value as the new head
  node of the list */
  addToHead(value) {
    const newNode = {
      value: value,
      prev: null,
      next: this.head
    };
    if (!this.tail && this.head) {
      this.tail = this.head;
      this.tail.prev = newNode;
    }
    if (this.head) {
      this.head.prev = newNode;
    }
    this.head = newNode;
  }

  /* Remove the list's current head. The list's
  `head` pointer should point to the removed node's
  `next` node */
  removeFromHead() {
    const result = this.head.value;
    const newHead = {
      value: this.head.next.value,
      prev: null,
      next: this.head.next.next
    };
    this.head = newHead;
    return result;
  }

  /* Adds the given value as the new tail
  node of the list */
  addToTail(value) {
    const newNode = {
      value: value,
      prev: this.tail,
      next: null
    };
    if (!this.head && this.tail) {
      this.head = this.tail;
      this.head.next = newNode;
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
    const result = this.tail.value;
    const newTail = {
      value: this.tail.prev.value,
      prev: this.tail.prev.prev,
      next: null
    };
    this.tail = newTail;
    return result;
  }

  /* Move the given node to the front of the
  list. Update the list's `head` pointer
  accordingly */
  moveToFront(node) {}

  /* Move the given node to the back of the
  list. Update the list's `tail` pointer 
  accordingly */
  moveToBack(node) {}

  /* Delete the given node from the list */
  delete(node) {}
}

module.exports = DoublyLinkedList;
