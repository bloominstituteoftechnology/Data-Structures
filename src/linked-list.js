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
      next: null,
    }
    // CASE: No Elements in LL - check to see if head is null -- if it is, then that means there are no elements in our Linked List
    if (this.head === null) { // can also simply write !this.head
      this.head = newNode;
      this.tail = newNode;
      return
    }
    // CASE: There are 1 or more elements in the LL
    // The value of newNode needs to define both (1) the deepest/last element in the linked list (this.tail) AND (2) the pointer to it
    // this.tail.next points to 
    this.tail.next = newNode;
    // update 'this.tail' to point to our new node
    this.tail = newNode;

  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {


  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {

  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    
  }
}

module.exports = LinkedList;

var myLL = new LinkedList();

console.log(myLL)
// CASE: No Elements in LL
myLL.addToTail(12);
console.log(myLL)
// CASE: Elements in LL
myLL.addToTail(5);
console.log(myLL)

myLL.addToTail(6);
console.log(myLL)
// You can see here that ALL the values, except the tail, are really stored in relation to the head.  Thus, you only have
// two assigned values (head and tail), and the rest can only be accessed by traversing the nested 'next's as see below
console.log(myLL.head)
console.log(myLL.head.next)
console.log(myLL.head.next.next)
console.log(myLL.head.next.next.next)

