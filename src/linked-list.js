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

class LinkedList {
  /* Do not modify the constructor */
  constructor() {
    this.head = null; // head and tail are an entire node 
    this.tail = null; 
  }

  /* Add the given value to the tail
  of the list. The `tail` pointer
  should be updated accordingly */
  addToTail(value) {
    const newNode = {
      value,
      next: null
    };
    // if there is no head, we're going to create a node as the head and as the tail
    if (this.head === null) {
      this.head = newNode;
      this.tail = newNode;
    }
    // Okay so this is referencing the point at which a node has been created already 
    // so we're changing the direction of this.tail.next to point to our new tail 
    this.tail.next = newNode; 
    this.tail = newNode; 
    
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
    if (!this.head) return null;
    // if our head is pointing to another node 
    if (this.head.next === null) {
      const value = this.head.value;
      this.head = null;
      this.tail = null;
      return value;
    }
    const removedHead = this.head.value;
    this.head = this.head.next;
    return removedHead;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let node = this.head;
    while (node) {
      if (node.value === value) return true;
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
