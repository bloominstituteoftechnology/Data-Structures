const List = require('./linked-list')

class Queue {
  /* Do not modify the constructor */
  constructor () {
    this.size = 0
    this.storage = new List()
  }

  /* Adds the given item to the queue */
  enqueue (item) {
    this.storage.shift(item)
  }

  /* Removes and returns the least recently
  added item from the queue */
  dequeue () {
    this.storage.unshift()
  }

  /* Returns true if the queue contains no
  elements, false otherwise */
  isEmpty () {
    if (this.storage.length === 0) {
      return true
    }
  }

  /* A getter method for the length of the queue */
  get length () {
    return this.storage.length
  }
}

module.exports = Queue
