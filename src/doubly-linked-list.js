class ListNode {
  /* Do not modify the constructor */
  constructor(value, prev = null, next = null) {
    this.value = value;
    this.prev = prev;
    this.next = next;
  }

  /* Insert the given node  as this node's
  `next` node */
  insertAfter(x) {



  }

  /* Insert the given value as the this node's
  `prev` node */
  insertBefore(x) {


  }

  /* Delete this node */
  delete() {

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
  addToHead(x) {
    let newNode = {
      value: x,
      next: this.head,
      prev: null,
    }
    this.head = newNode;

    if (!this.tail) {
      this.tail = newNode

    }


  }

  /* Remove the list's current head. The list's
  `head` pointer should point to the removed node's
  `next` node */
  removeFromHead() {
    if (!this.head) {

      return null;
    }

    let current = this.head;

    if (this.head) {
      this.head = this.head.next
    }
    if (this.head) {
      this.head.prev = null;
    }
    if (!this.head && this.tail) {
      this.tail = this.head
    }
    return current.value

  }

  /* Adds the given value as the new tail
  node of the list */
  addToTail(x) {
    const newNode = {
      value: x,
      prev: this.tail,

    }
    if (!this.head && !this.tail) {
      this.head = newNode;
      this.tail = newNode;
      return;
    }

    this.tail.next = newNode;
    this.tail = newNode

  }

  /* Remove the list's current tail. The list's
  `tail` pointer should point to the removed node's
  `prev` node */
  removeFromTail() {
    if (!this.tail) {
      return null;
    }

    let current = this.tail;
    let previous = this.tail.prev

    this.tail = previous;

    if (this.tail) {
      this.tail.next = null;
      this.tail.prev = previous.prev;
    }

    if (!this.tail && this.head) {
      this.head = this.tail
    }
    return current.value

  }

  /* Move the given node to the front of the
  list. Update the list's `head` pointer
  accordingly */
  moveToFront(node) {

    let current = node;
    let previous = node.prev
    let next = node.next;



    if (this.tail === node) {
      this.tail = previous
    }



    if (this.head) {
      node.next = this.head;
      node.prev = null
    }
    this.head = node;

    previous.next = next;

    next.prev = previous

      ;

    return node.value
  }

  /* Move the given node to the back of the
  list. Update the list's `tail` pointer 
  accordingly */
  moveToBack(node) {

  }

  /* Delete the given node from the list */
  delete(node) {

  }
}

module.exports = DoublyLinkedList;

// function Node(val) {
//   this.data = val;
//   this.prev = null;
//   this.next = null;
// }


// function LinkedList() {
//   this.head = null;
//   this.tail = null;

//   this.addAtFront = function (val) {
//     if (this.head === null) {  //If first node
//       this.head = new Node(val);
//       this.tail = this.head;
//     } else {
//       var temp = new Node(val);
//       temp.next = this.head;
//       this.head.prev = temp;
//       this.head = temp;
//     }
//   };

//   this.addAtEnd = function (val) {
//     if (this.tail === null) {  //If first node
//       this.tail = new Node(val);
//       this.head = this.tail;
//     } else {
//       var temp = new Node(val);
//       temp.prev = this.tail;
//       this.tail.next = temp;
//       this.tail = temp;
//     }
//   };

//   this.removeAtHead = function () {
//     var toReturn = null;

//     if (this.head !== null) {
//       toReturn = this.head.data;

//       if (this.tail === this.head) {
//         this.head = null;
//         this.tail = null;
//       } else {
//         this.head = this.head.next;
//         this.head.prev = null;
//       }
//     }
//     return toReturn;
//   };

//   this.removeAtTail = function () {
//     var toReturn = null;

//     if (this.tail !== null) {
//       toReturn = this.tail.data;

//       if (this.tail === this.head) {
//         this.head = null;
//         this.tail = null;
//       } else {
//         this.tail = this.tail.prev;
//         this.tail.next = null;
//       }
//     }

//     return toReturn;
//   };

//   this.each = function (f) {
//     var curr = this.head;
//     while (curr !== null) {
//       f(curr);
//       curr = curr.next;
//     }
//   };

//   this.printList = function () {
//     this.each(function (item) {
//       console.log(item.data);
//     });
//   };
// }

