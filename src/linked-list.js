class LinkedList {
  /* Do not modify the constructor */
  constructor() {
    this.head = null;
    this.tail = null;
  }

  /* Add the given value to the tail
  of the list. The `tail` pointer
  should be updated accordingly */
  addToTail(value) {
    const newNode = {
      value: value,
      next: null
    };
    // CASE 1: No Elements in LL - check to see if head is null -- if it is, then that means there are no elements in our Linked List
    if (this.head === null) {
      // can also simply write !this.head
      this.head = newNode;
      this.tail = newNode;
      return;
    }
    // CASE 2: There are 1 or more elements in the LL
    // If there is 1 or more element in the LL, then (this.tail) AND (this.tail.next) are already defined.  With a new value added,
    // these properties must be redefined.
    // The value of newNode needs to define both (1) the deepest/last element in the linked list (this.tail) AND (2) the pointer to it
    // (this.tail.next).
    this.tail.next = newNode;
    // update 'this.tail' to point to our new node
    this.tail = newNode;
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
    // CASE #1: There are no elements in the LL, thus there is no head
    if (this.head === null) return 'Error: This Linked List has no head';
    // CASE #2: There is one element in the LL, thus by removing the head, all this.head AND this.tail should effectively be
    // reset back to null
    if (this.head.next === null) {
      const value = this.head.value;
      this.head = null;
      this.tail = null;
      return value;
    }
    // CASE #3: There is more than one element in the LL, thus this.head must be set equal to the value of this.head.next.
    // This can be confusing if you think of this.head.next as a value, rather than what it is, which is the entire branch
    // structure, excluding only the top node, the head.  this.head = this.head.next effectively just cuts the first value
    // out by redefining 'head' as starting at this.head.next.
    const value = this.head.value; // only so that it can be returned as a confirmation that the correct head.value was removed
    this.head = this.head.next;
    return value;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    // CASE #1: No elements in the LL
    if (this.head === null) return false;
    // CASE #2: There are 1 of more elements in the LL
    // QUESTION: Is 'node' here a key word or a global variable? It is not defined, so I don't get how this works???
    // ANSWER: Notice that searchLinkedList is called below, and given the 'node' value of 'this.head'
    const searchLinkedList = node => {
      console.log(node);
      console.log(node.value);
      console.log(value);
      if (node.value === value) return true;
      if (node.next === null) return false;
      return searchLinkedList(node.next);
    };

    return searchLinkedList(this.head);
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    // CASE #1: No elements in LL
    if (this.head === null) return null;
    let largest = null;
    const findLargestValue = node => {
      // If largest has not been defined, then set it equal to node.value, otherwise, if this is not the
      // first iteration, and largest IS defined, then this will be skipped.
      if (largest === null) {
        let largest = node.value;
      }
      // if we are at the last iteration, and node === null, then return the value for largest
      if (!node) return largest;
      // if the current node.value is less than or equal to largest AND node.next exists, then run the next value -- node.next
      if (node.value <= largest && node.next) {
        return findLargestValue(node.next);
      }
      if (node.value > largest) {
        largest = node.value;
        return findLargestValue(node.next);
      }
      return largest;
    };
    return findLargestValue(this.head);
  }
}

module.exports = LinkedList;

// ========= myLL instance created ======== //
// var myLL = new LinkedList();
// console.log(myLL);

// ======= addToTail Method ======= //
// // CASE: No Elements in LL
// myLL.addToTail(12);
// console.log(myLL)
// console.log(myLL.head)
// console.log(myLL.head.next)
// console.log(myLL.tail)
// console.log(myLL.tail.next)
// // CASE: Elements in LL
// myLL.addToTail(5);
// console.log(myLL)
// console.log(myLL.tail.next)
// console.log(myLL.tail)
// myLL.addToTail(6);
// console.log(myLL)
// // You can see here that ALL the values, except the tail, are really stored in relation to the head.  Thus, you only have
// // two assigned values (head and tail), and the rest can only be accessed by traversing the nested 'next's as see below
// console.log(myLL.head)
// console.log(myLL.head.next)
// console.log(myLL.head.next.next)
// console.log(myLL.head.next.next.next)
// console.log(myLL.tail.next)

// ======= removeHead Method ======= //
// // CASE 1: Error sent as there is no head to remove.
// console.log(myLL.removeHead())
// // CASE 2:
// myLL.addToTail(1)
// console.log(myLL)
// console.log(myLL.removeHead())
// console.log(myLL)
// // CASE 3:
// myLL.addToTail(1)
// myLL.addToTail(2)
// myLL.addToTail(3)
// console.log(myLL)
// console.log(myLL.head)
// console.log(myLL.head.next)
// console.log(myLL.removeHead())
// console.log(myLL)
// console.log(myLL.head)
// console.log(myLL.head.next)

// ====== contains(value) method ======= //
// myLL.addToTail(1)
// myLL.addToTail(2)
// myLL.addToTail(3)
// console.log(myLL)
// console.log(myLL.contains(3))
// console.log(myLL.removeHead())

// ====== getMax() method ====== //
// console.log(myLL);
// console.log(myLL.getMax());
// myLL.addToTail(1);
// myLL.addToTail(2);
// myLL.addToTail(100);
// console.log(myLL.getMax());
