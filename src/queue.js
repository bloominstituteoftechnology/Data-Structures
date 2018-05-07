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
    if (this.isEmpty()) return null;
    this.size--;
    return this.storage.removeHead();
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

// const q = new Queue();
// q.enqueue(1);
// q.enqueue(2);
// q.enqueue(3);
// q.enqueue(4);
// const x = q.dequeue();

// console.log(q, '++++++', x);
module.exports = Queue;
