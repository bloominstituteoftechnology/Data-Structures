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
      next: null,
      value: value,
    };

    // if there is no node just return null- just incase we have a list with no nodes
    if (this.head === null) {
      this.head = newNode;
      this.tail = newNode;
      return;
    }
    // If there is one element in the list before the new element is added, the new element becomes the tail of the list
    this.tail.next = newNode; // our new node is now the tail (this.tail.next is referencing the old node)
    this.tail = newNode; // update the tail of the linkedlist itself in the constructor 
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
    if (this.head === null) return this.head = null;
    // check if head has a next
    if (this.head.next === null) {
      const value = this.head.value;
      this.head = null;
      this.tail = null;
      return value;
    }
    const value = this.head.value;
    this.head = this.head.next;
    return value;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let node = this.head;
    while (node !== null) {
      if (node.value == value) return true;
      node = node.next;
    }
    return false;
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    let node = this.head;
    let max = null;
    while (node) {
      if (node.value > max) {
        max = node.value;
      }
      node = node.next;
    }
    return max;
  }
}

module.exports = LinkedList;


// const list = {
//   head: {
//       value: 12
//       ,next: {
//           value: 99
//           ,next: {
//               value: 37
//               ,next: null
//           }
//       }
//   }
// };