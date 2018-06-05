/* 
  For your Queue implementation, you'll use 
  your Linked List implementation to construct
  the Queue.
*/
const List = require("./linked-list");

class Queue {
  /* Do not modify the constructor */
  constructor() {
    this.size = 0;
    this.storage = new List();
  }

  /* Adds the given item to the queue */
  enqueue(item) {
    let node = {
      value: item,
      next: null
    };
    // think queue front as head and rear as tail;

    if (this.storage.head == null) {
      this.storage.head = node;
      this.storage.tail = node;
    } else {
      this.storage.tail.next = node;
      this.storage.tail = node;
    }
    this.size++;
    // console.log(this.storage);
  }

  /* Removes and returns the least recently
  added item from the queue */
  dequeue() {
    // alternatively, you can import and use removeHead() 
    // function from linked-list.js

    if (this.isEmpty() == true) {
      return null;
    } else if (this.isEmpty != true) {
      let deleted = this.storage.head;
      this.storage.head = deleted.next;
      this.size--;
      return deleted.value;
    }
  }

  /* Returns true if the queue contains no
  elements, false otherwise */
  isEmpty() {
    if (this.storage.head == null) {
      return true;
    } else {
      return false;
    }
  }

  /* A getter method for the length of the queue */
  get length() {
    return this.size;
  }
}

module.exports = Queue;
