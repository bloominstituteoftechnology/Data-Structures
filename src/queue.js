const List = require('./linked-list');

class Queue {
  /* Do not modify the constructor */
  constructor() {
    this.size = 0;
    this.storage = new List();
  }

  /* Adds the given item to the queue */
  enqueue(item) {
    // this.storage[this.size] = item;
    // this.size++;

    this.storage.addToTail(item);
    return this.size++;
  }

  /* Removes and returns the least recently
  added item from the queue */
  dequeue() {

    if(this.storage.head === null){
      return null;
    }
    if(this.storage.size === 0){
      return null;
    }
    return this.storage.removeHead();

  }

  /* Returns true if the queue contains no
  elements, false otherwise */
  isEmpty() {
    if (this.storage.head === null){
      return false;
    }
    else true;
  }

  /* A getter method for the length of the queue */
  get length() {
    return this.size;
  }
}

module.exports = Queue;