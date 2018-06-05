const Queue = require("../src/queue");

let queue;

describe("Queue", () => {
  beforeEach(() => {
    queue = new Queue();
  });

  it('should have the methods "enqueue", "dequeue", "isEmpty", and a "length" getter', () => {
    expect(Object.getPrototypeOf(queue).hasOwnProperty("enqueue")).toBe(true);
    expect(Object.getPrototypeOf(queue).hasOwnProperty("dequeue")).toBe(true);
    expect(Object.getPrototypeOf(queue).hasOwnProperty("isEmpty")).toBe(true);
    expect(Object.getPrototypeOf(queue).hasOwnProperty("length")).toBe(true);
  });

  it("should return a size of 0 for an empty queue", () => {
    expect(queue.length).toBe(0);
  });

  it("should return the correct size after queuing items", () => {
    queue.enqueue(null);
    queue.enqueue(null);
    queue.enqueue(null);
    queue.enqueue(null);
    queue.enqueue(null);
    queue.enqueue(null);
    queue.enqueue(null);
    queue.enqueue(null);
    queue.enqueue(null);
    queue.enqueue(null);
    expect(queue.length).toBe(10);
  });

  it('should return "null" when attempting to dequeue from an empty queue', () => {
    expect(queue.dequeue()).toBeNull();
  });

  it("should return a size of 0 after attempting to dequeue more items than were queued", () => {
    queue.dequeue();
    queue.dequeue();
    queue.dequeue();
    expect(queue.length).toBe(0);
  });

  it("should dequeue and return the top item", () => {
    queue.enqueue(1);
    expect(queue.dequeue()).toBe(1);
  });

  it("should dequeue the first item queued if multiple items were queued", () => {
    queue.enqueue(true);
    queue.enqueue("hi");
    queue.enqueue(null);
    queue.enqueue(77);
    expect(queue.dequeue()).toBe(true);
  });

  it("should respect the order with which elements are queued", () => {
    queue.enqueue(true);
    queue.enqueue("hi");
    queue.enqueue(null);
    queue.enqueue(77);
    expect(queue.dequeue()).toBe(true);
    expect(queue.dequeue()).toBe("hi");
    expect(queue.dequeue()).toBe(null);
    expect(queue.dequeue()).toBe(77);
  });
});
