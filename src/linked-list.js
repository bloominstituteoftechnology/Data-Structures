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
if(!this.head) {
  this.head = newNode;
  this.tail = newNode;
  return;
}
this.tail.next = newNode;
this.tail = newNode;
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
  if(!this.head) return null;
  let value = this.head.value;
  this.head = this.head.next;
  if(this.head) this.head.prev = null;
  else this.tail = null;
  return value;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let cur = this.head;
    while(cur) {
      if(cur.value === value) return true;
      cur = cur.next;
    }
    return false;
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    let value = null;
    let cur = this.head;
    while(cur) {
      if(cur.value > value)
      value = cur.value;
      cur = cur.next;
    }
    return value;
  }
}

module.exports = LinkedList;