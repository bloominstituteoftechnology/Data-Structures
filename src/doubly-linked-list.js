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
    if(!this.head) {
      const newNode = new ListNode(value, null, null);
      this.head = newNode;
      this.tail = newNode;
    } else {
      const newNode = new ListNode(value, null, this.head);
      this.head.insertBefore(newNode);
      this.head = newNode;
    }
  }

  /* Remove the list's current head. The list's
  `head` pointer should point to the removed node's
  `next` node */
  removeFromHead() {
    if(!this.head) {
      return null;
    } else {
      const head = this.head;
      this.head = head.next;
      if(this.head) {
        this.head.insertBefore(null);
      }
      head.delete()
      return head.value;
    }
  }

  /* Adds the given value as the new tail
  node of the list */
  addToTail(value) {
    const newNode = new ListNode(value, this.tail, null);
    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.tail.insertAfter(newNode);
      this.tail = newNode;
    }
  }

  /* Remove the list's current tail. The list's
  `tail` pointer should point to the removed node's
  `prev` node */
  removeFromTail() {
    if (!this.tail) {
      return null;
    }
    if(!this.tail.prev) {
      const value = this.tail.value;
      this.head = null;
      this.tail = null;
      return value;
    }
    const tail = this.tail;
    this.tail = tail.prev;
    this.tail.insertAfter(null);
    tail.delete();
    return tail.value;
  }

  /* Move the given node to the front of the
  list. Update the list's `head` pointer
  accordingly */
  moveToFront(node) {
    if (node === this.tail) {
      this.tail = node.prev;
    }
    if (node.next) {
      node.next.insertBefore(node.prev);
    }
    if (node.prev) {
      node.prev.insertAfter(node.next);
    }
    this.addToHead(node.value);
  }

  /* Move the given node to the back of the
  list. Update the list's `tail` pointer 
  accordingly */
  moveToBack(node) {
    if (node === this.head) {
      this.head = node.next;
    } 
    if(node.next) {
      node.next.insertBefore(node.prev);
    }
    if(node.prev){
      node.prev.insertAfter(node.next);
    }
    this.addToTail(node.value);
  }

  /* Delete the given node from the list */
  delete(node) {
    if (node === this.head) {
      this.head = node.next;
    }
    if (node === this.tail){
      this.tail = node.prev;
    }
    if (node.next) {
      node.next.insertBefore(node.prev);
    }
    if (node.prev) {
      node.prev.insertAfter(node.next);
    }
  }
}

module.exports = DoublyLinkedList;