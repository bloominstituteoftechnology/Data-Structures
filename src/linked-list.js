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
    };
    if (!this.head) {
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
  removeHead(value) {
    if(!this.head){ 
      return null;
    }
    
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    if (!this.head){
      return;

    }
    let mymyObj = this.head;
    while(mymyObj){
      if(mymyObj.value === value) return true;
      mymyObj = mymyObj.next;
    }
    return false;

  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    if(!this.head) {
      return null;
    }
    let max = 0;
    let myObj =this.head;
    while(myObj){
      if(max < myObj.value){
        console.log(max);
        max = myObj.value;
        console.log(max);
              }
              console.log(myObj.value);
              myObj = myObj.next;
    }
    return max;
  }
}

module.exports = LinkedList;