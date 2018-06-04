const List = require('./linked-list');

class Queue {
  /* Do not modify the constructor */
  constructor() {
    this.size = 0;
    this.storage = new List();
  }

  /* Adds the given item to the queue */
  enqueue(item) {
    console.log('enqueuing', item, this.storage);
    this.storage.addToTail(item);
    this.size++;
  }

  /* Removes and returns the least recently
  added item from the queue */
  dequeue() {
    if (this.size === 0) {
      return null;
    } else {
      const removed = this.storage.head.value;
      this.storage.removeHead();
      this.size--;
      return removed;
    }
  }

  /* Returns true if the queue contains no
  elements, false otherwise */
  isEmpty() {
    return this.size === 0;
  }

  /* A getter method for the length of the queue */
  get length() {
    return this.size;
  }
}

module.exports = Queue;