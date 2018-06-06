const List = require('./linked-list');



class Queue {
  /* Do not modify the constructor */
  constructor() {
    this.size = 0;
    this.storage = new List();


  }

  /* Adds the given item to the queue */
  enqueue(item) {

    this.storage.addToTail(item)
    this.size++;

  }

  /* Removes and returns the fist added  
  added item to the queue */
  dequeue() {
    if (this.isEmpty()) {
      return null;
    }
    else {
      let removedItem = this.storage.removeHead();
      this.size--;
      return removedItem;
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

