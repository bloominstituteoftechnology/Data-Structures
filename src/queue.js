const List = require("./linked-list");

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
    let myQ = this.storage.head;
    if (!myQ) return null;
    let dequeued = myQ;
    myQ = myQ.next;
    this.size--;
    return dequeued.value;
  }

  /* Returns true if the queue contains no
  elements, false otherwise */
  isEmpty() {
    if (this.size === 9) return true;
    else return false;
  }

  /* A getter method for the length of the queue */
  get length() {
    return this.size;
  }
}

module.exports = Queue;
