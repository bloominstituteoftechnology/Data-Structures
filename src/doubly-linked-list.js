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
    this.node = null;
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
      this.head = new ListNode(value);
      this.tail = this.head;
    } else {
      const oldHead = this.head;
      const newHead = new ListNode(value, null, oldHead);
      this.head = newHead;
      oldHead.prev = this.head;
    }
  }

  /* Remove the list's current head. The list's
  `head` pointer should point to the removed node's
  `next` node */
  removeFromHead() {
    if (!this.head) return null;
    const oldHead = { ...this.head };
    if (!this.head.next) {
      this.head = null;
      this.tail = null;
    } else {
      this.head = this.head.next;
      this.head.prev = null;
    }
    return oldHead.value;
  }

  /* Adds the given value as the new tail
  node of the list */
  addToTail(value) {
    if (!this.tail) {
      this.tail = new ListNode(value);
      this.head = this.tail;
    } else {
      const oldTail = this.tail;
      const newTail = new ListNode(value, oldTail, null);
      this.tail = newTail;
      oldTail.next = this.tail;
    }
  }

  /* Remove the list's current tail. The list's
  `tail` pointer should point to the removed node's
  `prev` node */
  removeFromTail() {
    if (!this.tail) return null;
    const oldTail = { ...this.tail };
    if (!this.tail.prev) {
      this.tail = null;
      this.head = null;
    } else {
      this.tail = this.tail.prev;
      this.tail.next = null;
    }
    return oldTail.value;
  }

  /* Move the given node to the front of the
  list. Update the list's `head` pointer
  accordingly */
  moveToFront(node) {
    if (this.head === node) return;
    if (node.next) {
      node.next.prev = node.prev;
      node.prev.next = node.next;
    } else {
      this.tail = node.prev;
      this.tail.next = null;
    }
    this.head.prev = node;
    node.prev = null;
    node.next = this.head;
    this.head = node;
  }

  /* Move the given node to the back of the
  list. Update the list's `tail` pointer 
  accordingly */
  moveToBack(node) {
    //redundancy check
    if (this.tail === node) return;
    if (node.prev) {
      //step out
      node.next.prev = node.prev;
      node.prev.next = node.next;
    } else {
      //step off the end
      this.head = node.next;
      this.head.prev = null;
    }
    //update tail, node, and list
    this.tail.next = node;
    node.next = null;
    node.prev = this.tail;
    this.tail = node;
  }

  /* Delete the given node from the list */
  delete(node) {
    if (node.next) {
      if (node.prev) {
        //prev and next - update adjacent node references only
        node.prev.next = node.next;
        node.next.prev = node.prev;
      } else {
        //next but no prev (head) - update next and list head
        node.next.prev = null;
        this.head = node.next;
      }
    } else {
      if (node.prev) {
        //prev but no next (tail) - update previous and list tail
        node.prev.next = null;
        this.tail = node.prev;
      } else {
        //no prev no next (head/tail) - update list head and tail
        this.head = null;
        this.tail = null;
      }
    }
  }
}

module.exports = DoublyLinkedList;