class Node {
  constructor(value=null, nextNode=null) {
    this.value = value;
    this.nextNode = nextNode;
  }

  getValue() {
    return this.value;
  }

  getNext() {
    return this.nextNode;
  }

  setNext(newNext) {
    this.nextNode = newNext
  }
}

class LinkedList {
  constructor(){
    this.head = null;
    this.tail = null;
  }

  addToTail(value) {
    const newNode = new Node(value);
    if(this.tail) {
      this.tail.setNext(newNode);
    }
    if(!this.head) {
      this.head = newNode;
    }
    this.tail = newNode
  }

  removeHead() {
    const oldHead = this.head;
    let returnValue = null;
    if(this.head){
      if(this.head === this.tail) {
        returnValue = oldHead.getValue();
        this.head = null;
        this.tail = null;
      } else {
        const newHead = oldHead.getNext();
        this.head = newHead
        returnValue = oldHead.getValue();
      }
    }
    return returnValue;
  }

  contains(value) {
    let found = false;
    if(this.head) {
      let current = this.head;
      if(this.head === this.tail) {
        if(this.head.getValue() === value) {
          found = true;
        }
      } else {
        while(current && found === false) {
          if(current.getValue() === value){
            found = true;
          }
          current = current.getNext()
        }
      }
    }
    return found
  }

  getMax() {
    let max = null;
    if(this.head) {
      let current = this.head;
      if(this.head === this.tail) {
        max = this.head.getValue()
      } else {
        while(current){
          if(!max || current.getValue() > max) {
            max = current.getValue();
          }
          current = current.getNext();
        }
      }
    }
    return max;
  }
}

const myList = new LinkedList();
//TEST: adding to tail
// myList.addToTail(1);
// console.log('1:', myList.head.getValue());
// console.log('1:', myList.tail.getValue());
// myList.addToTail(2);
// console.log('2:', myList.tail.getValue());
// console.log('1:', myList.head.getValue());

//TEST: contains
// myList.addToTail(1);
// myList.addToTail(2);
// myList.addToTail(5);
// myList.addToTail(10);
// console.log('True:', myList.contains(10));
// console.log('True:', myList.contains(2));
// console.log('False:', myList.contains(1000));

//TEST remove head
// myList.addToTail(10);
// myList.addToTail(20);
// console.log('10:', myList.removeHead());
// console.log('False:', myList.contains(10));
// console.log('20:', myList.removeHead());
// console.log('False:', myList.contains(20));
//
// myList.addToTail(10);
// console.log('10:', myList.removeHead(10));
// console.log('null:', myList.head);
// console.log('null:', myList.tail);
// console.log('null:', myList.removeHead())

//TEST getMax()
// console.log('null:', myList.getMax());
// myList.addToTail(100);
// console.log('100:', myList.getMax());
// myList.addToTail(55);
// console.log('100:', myList.getMax());
// myList.addToTail(101);
// console.log('101:', myList.getMax());
