class Node{
  constructor(v = null){
    this.value = v;
    this.next = null;
  }
  setNext(n){
    this.next = n;
  }
  setValue(v){
    this.value = v;
  }
}
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
    if(!this.head){
      this.head = this.tail = new Node(value);
    }
    else{
      this.tail.next = new Node(value);
      this.tail = this.tail.next;
    }
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
