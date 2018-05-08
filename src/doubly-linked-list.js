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
        // first check to see if head or tail are null
        if (!this.head || !this.tail) {
            // if so set them to a list node
            this.head = new ListNode(value);
            this.tail = new ListNode(value);
            // otherwise insert value as head and
        } else {
            this.head.insertBefore(value);
            console.log("HEAD", this.head);
            this.head = this.head.prev;
        }
    }

    /* Remove the list's current head. The list's
  `head` pointer should point to the removed node's
  `next` node */
    removeFromHead() {
        if (this.head) {
            const val = this.head.value;
            this.head = this.head.next;
            return val;
        }
        return null;
    }

    /* Adds the given value as the new tail
  node of the list */
    addToTail(value) {
        if (!this.tail || !this.head) {
            this.head = new ListNode(value);
            this.tail = new ListNode(value);
        } else {
            this.tail.insertAfter(value);
            this.tail = this.tail.next;
        }
    }

    /* Remove the list's current tail. The list's
  `tail` pointer should point to the removed node's
  `prev` node */
    removeFromTail() {
        if (this.tail) {
            const val = this.tail.value;
            this.tail = this.tail.prev;
            return val;
        }
        return null;
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

const newDoubly = new DoublyLinkedList();
newDoubly.addToHead(10);
newDoubly.addToHead(12);
newDoubly.addToTail(11);

// console.log("LINE 77", newDoubly);

module.exports = DoublyLinkedList;
