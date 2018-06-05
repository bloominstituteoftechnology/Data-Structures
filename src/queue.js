const List = require('./linked-list');

class Queue {
  /* Do not modify the constructor */
  constructor() {
    this.size = 0;
    this.storage = new List();
  }

  /* Adds the given item to the queue */
  enqueue(item) {
    this.size++;
    this.storage.addToTail(item);
  }

  /* Removes and returns the least recently
  added item from the queue */
  dequeue() {

    if(this.size === 0) {
      return null
    }
    this.size--
    let temp = this.storage.head;
    this.storage.removeHead();
    return temp.value
  }

  /* Returns true if the queue contains no
  elements, false otherwise */
  isEmpty() {

    if(this.size === 0) {
      return true
    }

    return false;

  }

  /* A getter method for the length of the queue */
  get length() {
    return this.size;
  }
}

module.exports = Queue;