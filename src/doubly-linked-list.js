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
    const newNode = new ListNode(value);
    newNode.prev = this;
    this.next = newNode;
  }

  /* Insert the given value as the this node's
  `prev` node */
  insertBefore(value) {
    const newNode = new ListNode(value);
    newNode.next = this;
    this.prev = newNode;
  }

  /* Delete this node */
  delete() {
    let currentNode = this;
    let nodeBefore = this.prev;
    let nodeAfter = this.next;
    
    // check if mid, head, or tail node
    if (nodeBefore && nodeAfter) {
      nodeAfter.prev = this.prev;
      nodeBefore.next = this.next;
    } else if (nodeAfter) {
      nodeAfter.prev = null;
    } else {
      nodeBefore.next = null;
    }

    // delete self
    currentNode = null;
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
    let currentHead = this.head;
    let newHead = new ListNode(value);
    
    // check if this is first node
    if (!currentHead) {
      this.head = newHead;
      this.tail = newHead;
      return;
    }
    
    // otherwise, link appropriately
      this.head = newHead;
      currentHead.prev = newHead;
      newHead.next = currentHead;
  }

  /* Remove the list's current head. The list's
  `head` pointer should point to the removed node's
  `next` node */
  removeFromHead() {    
    if (!this.head) return null;

    let value = this.head.value;

    if (this.head === this.tail) {
      this.head = null;
      this.tail = null;
    } else {
      this.head = this.head.next;
      this.head.prev = null;
    }
    
    return value;
  }

  /* Adds the given value as the new tail
  node of the list */
  addToTail(value) {
    let currentTail = this.tail;
    let newTail = new ListNode(value);
    
    // if first node
    if (!this.head) {
      this.head = newTail;
      this.tail = newTail;
      return;
    }

    // otherwise
    currentTail.next = newTail;
    newTail.prev = currentTail;
    this.tail = newTail;
  }

  /* Remove the list's current tail. The list's
  `tail` pointer should point to the removed node's
  `prev` node */
  removeFromTail() {
    if (!this.tail) return null;
    let currentTail = this.tail;
    
    if (currentTail === this.head) {
      this.head = null;
      this.tail = null;
    } else if (currentTail.prev === this.head) {
      this.tail = this.head;
      this.tail.next = null;
    } else {
      let newTail = currentTail.prev;
      newTail.next = null;
    }

    return currentTail.value;
  }

  /* Move the given node to the front of the
  list. Update the list's `head` pointer
  accordingly */
  moveToFront(node) {
    if (!node.prev) return;
    
    let leftNode = node.prev;
        
    if (!node.next) {
      leftNode.next = null;
      this.tail = leftNode;
    } else {
      let rightNode = node.next;
      leftNode.next = rightNode;
      rightNode.prev = leftNode;
    }
    
    this.head.prev = node;
    node.next = this.head;
    node.prev = null;
    this.head = node;
  }

  /* Move the given node to the back of the
  list. Update the list's `tail` pointer 
  accordingly */
  moveToBack(node) {
   if (!node || !node.next) return;
   
   let rightNode = node.next;

   if (!node.prev) {
     rightNode.next = null;
     this.head = rightNode;
   } else {
     let leftNode = node.prev;
     rightNode.next = leftNode;
     leftNode.prev = rightNode;
   }

   this.tail.next = node;
   node.prev = this.tail;
   node.next = null;
   this.tail = node;
  }

  /* Delete the given node from the list */
  delete(node) {
    node.next.prev = node.prev;
    node.prev.next = node.next;
  }
}

module.exports = DoublyLinkedList;
