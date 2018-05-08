const List = require('./linked-list');

class Queue {
  /* Do not modify the constructor */
  constructor() {
    this.size = 0;
    this.storage = []
  }

  /* Adds the given item to the queue */
  enqueue(item) {
    this.storage.push(item)
    this.size++
  }

  /* Removes and returns the least recently
  added item from the queue */
  dequeue() {
    if (this.length === 0) return null;
    let mem = this.storage[0]
    this.storage.shift()
    this.size--
    return mem
  } 

  /* Returns true if the queue contains no
  elements, false otherwise */
  isEmpty() {
    if (this.size === 0) return true;
    return false;
  }

  /* A getter method for the length of the queue */
  get length() {
    return this.storage.length;
  }
}

module.exports = Queue;

// // ========= myLL instance created ======== //
// var myQ = new Queue();
// console.log(myQ);
// // ===== enque() method tested ====== //
// myQ.enqueue(1)
// console.log(myQ)
// myQ.enqueue(10)
// console.log(myQ)
// // ====== dequeue() method tested ====== //
// myQ.dequeue()
// console.log(myQ)
// // ======= isEmpty() ======= //
// console.log(myQ.isEmpty())
// myQ.dequeue()
// console.log(myQ.isEmpty())
// // ====== get length() ======= //
// console.log(myQ.length)
// myQ.enqueue(10)
// myQ.enqueue(11)
// myQ.enqueue(12)
// console.log(myQ.length)
// console.log(myQ.size)

