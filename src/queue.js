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

// const newQ = new Queue();
// newQ.enqueue(1);
// newQ.enqueue(2);
// newQ.enqueue(3);
// console.log("===", newQ);

module.exports = Queue;
