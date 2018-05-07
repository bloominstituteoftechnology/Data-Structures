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
    let val = this.head.value;
    this.head = this.head.next;
    return val;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let current = this.head;
    let found = false;
    while(current){
      if(current.value === value){
        return true;
      }
      current = current.next;
    }
    return false;
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    if(this.head){
      let current = this.head;
      let max = current.value;
      while(current){
        if(current.value > max){
          max = current.value;
        }
        current = current.next;
      }
      return max;
    }
    else{
      return null;
    }
  }
}

module.exports = LinkedList;
