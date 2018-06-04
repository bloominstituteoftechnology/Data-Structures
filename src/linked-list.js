class LinkedList {
  /* Do not modify the constructor */
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
    this.count = 0;
  }

  /* Add the given value to the tail
  of the list. The `tail` pointer
  should be updated accordingly */
  addToTail(value) {
    const node = {value};
    this.length++;
    if (!this.head) {
     this.head = node;
    }
    else {
      this.tail.next = node;
    }
    this.tail = node;















    // const newHeadNod = {value};
    
    // newHeadNod.next = this.head;
    // this.tail = newHeadNod;
    // if (this.head === null) {
      
    //   this.head = newHeadNod;
    // } else {

    // }
    // this.length++;
    // this.addToTail

    // return this;
//<<<<
// const node = {
//   data: value,
//   next: null
// }

// if(this.count === 0) {
//   // If this is the first Node, assign it to head
//   this.head = node;
// } else {
//   // If not the first node, link it to the last node
//   this.tail.next = node;
// }

// this.tail = node;

// this.count++;
// return this
//>>>
      // Create a new Node
      // const node = new LinkedList(value);
      // // this.length++;
      // if (!this.head) {
      //  this.head = node;
      // }
      // else {
      //   this.tail.next = node;
      // }
      // this.tail = node;
      // return this
  }

  /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
  removeHead() {
    if (this.length === 0) {
        return undefined;
    }
    const value = this.head.value;
    this.head = this.head.next;
    this.length--;
    return value;
    //<<<>>>>
 

  }

  /* Searches the list for the given value
  Returns true or false accordingly */
  contains(value) {
    let thisNode = this.head;
 
    while(thisNode) {
        if(thisNode.value === value) {
            return true;
        }
         else {
          return false
        }
            
        thisNode = thisNode.next;
    }
     
    return thisNode;


//><<<<<<<<<

// if (!this.head) return null;
//     if (this.head === this.tail) {
//       const node = this.head;
//       this.head = this.tail = null;
//       return node.value;
//     }
    // const penultimate = this._find(null, (value, nodeValue, i, current) => current.next === this.tail );
    // const ans = penultimate.next.value;
    // penultimate.next = null;
    // this.tail = penultimate;
    // this.length--;
    // return ans;

  }

  /* Finds and returns the maximal value
  of all the values in the list */
  getMax() {
    let thisNode = this.head;
    let val = thisNode.value;
    while(thisNode) {
        if(thisNode.value >= val) {
         return console.log('greater:', thisNode.value)
          return  val = thisNode.value;
        }
        //  else {
        //   return false
        // }
            
        thisNode = thisNode.next;
    }
     
    return val;
    
  }
}

module.exports = LinkedList;