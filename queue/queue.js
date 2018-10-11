const LinkedList = require('../linked_list/linked_list.js');

class Queue {
  constructor() {
    this.size = 0;
    this.storage = new LinkedList();
  }

  enqueue(item) {
    this.storage.addToTail(item);
    this.size++;
  }

  dequeue() {
    const removed = this.storage.removeHead();
    if(removed) this.size--;
    return removed;
  }

  length() {
    return this.size;
  }
}

const myQueue = new Queue();
//TEST empty queue
// console.log('0:', myQueue.length());

//TEST length after queue
// console.log('0:', myQueue.length());
// myQueue.enqueue(2);
// console.log('1:', myQueue.length());
// myQueue.enqueue(4);
// console.log('2:', myQueue.length());
// myQueue.enqueue(6);
// myQueue.enqueue(8);
// myQueue.enqueue(10);
// myQueue.enqueue(12);
// myQueue.enqueue(14);
// myQueue.enqueue(16);
// myQueue.enqueue(18);
// console.log('9:', myQueue.length());

//TEST empty dequeue
// console.log('null:', myQueue.dequeue());
// console.log('0:', myQueue.length());

//TEST dequeue respects order
myQueue.enqueue(100);
myQueue.enqueue(101);
myQueue.enqueue(105);
console.log('100:', myQueue.dequeue());
console.log('2:', myQueue.length());
console.log('101:', myQueue.dequeue());
console.log('1:', myQueue.length());
console.log('105:', myQueue.dequeue());
console.log('0:', myQueue.length());
console.log('null:', myQueue.dequeue());
console.log('0:', myQueue.length());
