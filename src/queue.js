const List = require('./linked-list');

class Queue {
  /* Do not modify the constructor */
  constructor() {
    this.size = 0;
    this.storage = new List();
  }

  /* Adds the given item to the queue */
  enqueue(item) {
    this.storage.addToTail(item);
    this.size++;
  }

  /* Removes and returns the least recently
  added item from the queue */
  dequeue() {
    this.storage.removeHead(item);
    this.size++;
  }

  /* Returns true if the queue contains no
  elements, false otherwise */
  isEmpty() {
    if(this.size===10) return true;
    else return false;
  }

  /* A getter method for the length of the queue */
  get length() {

  }
}

module.exports = Queue;