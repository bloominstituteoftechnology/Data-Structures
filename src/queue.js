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
    return this.storage.addToTail(item);
  }

  /* Removes and returns the least recently
  added item from the queue */
  dequeue() {
    if (!this.size) return null;
    this.size--;
    return this.storage.removeHead();
  }

  /* Returns true if the queue contains no
  elements, false otherwise */
  isEmpty() {
    // if (this.size !== 0) {
    //   return true;
    // } else {
    //   return false;
    // }
    return this.size; // if 0 it'll be false if anything other then 0 its a truthy value
  }

  /* A getter method for the length of the queue */
  get length() {
    return this.size;
  }
}

module.exports = Queue;
