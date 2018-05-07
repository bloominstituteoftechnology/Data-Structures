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
  removeHead() {
    let rem = this.head;
    this.head = this.head.next;
    return rem.value;
  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
  //   let start = this.head;
  //   let end = this.tail;
  //   let ans;
  //   for(let i = start.length; i < end.length; i++) {
  //     if(start[i] == value){
  //       ans = true;
  //     }
  //     else ans = false;
  //   }
  //   return ans;

    let ans = this.head;
    while(ans) {
      if (ans.value === value) return true;
      ans = ans.next;
    }
    return false;

  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
  //   let sumUp = this.head;

  //   if (sumUp === null){
  //     return null;
  // } 
  //   else{
  //     while(sumUp.next !== null){
  //       sumUp += sumUp.next;
  //   }
  //   return sumUp;
  //   }
  // }

  let sum = this.head;
  let maxSum = null;

  while(sum) {
    if(sum.value > maxSum){
      maxSum = sum.value;
    }
    sum = sum.next;
  }
  return maxSum;
}
}

module.exports = LinkedList;