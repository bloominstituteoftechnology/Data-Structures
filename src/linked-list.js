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
      value,
      next: null
    }

    if(this.head === null){
      this.head = newNode;
    }
    if (this.tail !== null){
      this.tail.next = newNode;
    }

    this.tail = newNode;
    return this;
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
    let tempHead = this.head;
    this.head = this.head.next;
    return tempHead.value;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    if (this.head.value === value) return true;
    let node = this.head.next;
    do{
      if (node.value === value) return true;
      else node = node.next;
    } while(node);
    return false;
  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    let maxNum = 0;
    // console.log("getMax this: ", this);
    if(this.head !== null) {
      if (this.head.value > maxNum) {
        maxNum = this.head.value;
      };
      
      if(this.head.next){
        let node = this.head.next;
        
        do{
          if(node.value > maxNum) maxNum = node.value;
          node = node.next;
        } while(node);
      }
      return maxNum;
    } else {
      return null;
    }
  }
}

module.exports = LinkedList;

const list = new LinkedList();
list.addToTail(1);
list.addToTail(2);
list.addToTail(5);
list.addToTail(10);
console.log(list); 