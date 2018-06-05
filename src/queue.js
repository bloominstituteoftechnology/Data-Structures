/* 
  For your Queue implementation, you'll use 
  your Linked List implementation to construct
  the Queue.
*/
const List = require('./linked-list');
class Queue {
  /* Do not modify the constructor */
  constructor() {
    this.size = 0;
    this.storage = new List();
  }
  
  /* Adds the given item to the queue */
  enqueue(item) {
    //* `enqueue` should add an item to the back of the queue.
    this.storage.addToTail(item);
    this.size++
   
  }
  
  /* Removes and returns the least recently
  added item from the queue */
  dequeue() {
    //* `dequeue` should remove and return an item from the front of the queue.
    
    if (this.size > 0) {
      this.size--
      return this.storage.removeHead()
    } 
   
   this.size 
    return null
  }
  
  /* Returns true if the queue contains no
  elements, false otherwise */
  isEmpty() {
    //* `isEmpty` should return `true` if the queue contains no elements, `false` otherwise.
  
    if (this.isEmpty() && this.size ===  0) {
      return true
    } else {
      false
    }
    //this.storage.contains 
    
  }
  
  /* A getter method for the length of the queue */
  get length() {
  //* A `length` getter that returns the number of items in the queue.
 
    return this.size
  }
}

module.exports = Queue;
