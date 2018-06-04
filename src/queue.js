/* 
  For your Queue implementation, you'll use 
  your Linked List implementation to construct
  the Queue.
*/
const List = require('./linked-list');

class Queue {
  /* Do not modify the constructor */
  constructor() {
    this.size = 0;
    this.storage = new List();
  }

  /* Adds the given item to the queue */
  enqueue(item) {
    // this.storage.enqueue.push(item);
    // return this
    // this.storage = [...this.storage, item]
    this.storage.push(item)
    // this.size++;
    return this.storage
  }

  /* Removes and returns the least recently
  added item from the queue */
  dequeue() {
    this.storage.pop();
    return this.storage
  }

  /* Returns true if the queue contains no
  elements, false otherwise */
  isEmpty() {

  }

  /* A getter method for the length of the queue */
  get length() {

  }
}
// Queue.enqueue(0)

module.exports = Queue;
