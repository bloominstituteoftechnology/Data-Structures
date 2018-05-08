const Heap = require('../src/heap');

let heap;

describe('Heap', () => {
  beforeEach(() => {
    heap = new Heap();
  });

  it('should have methods named "insert", "delete", "getMax", "getSize", "bubbleUp", and "siftDown"', () => {
    expect(typeof heap.insert).toBe('function');
    expect(typeof heap.delete).toBe('function');
    expect(typeof heap.getMax).toBe('function');
    expect(typeof heap.getSize).toBe('function');
    expect(typeof heap.bubbleUp).toBe('function');
    expect(typeof heap.siftDown).toBe('function');
  });

  it('should get the max value of the heap elements', () => {
    heap.insert(6);
    heap.insert(8);
    heap.insert(10);
    heap.insert(9);
    heap.insert(1);
    heap.insert(9);
    heap.insert(9);
    heap.insert(5);
    expect(heap.getMax()).toEqual(10);
  });

  it('should properly get the new max after the old max is deleted', () => {
    heap.insert(6);
    heap.insert(8);
    heap.insert(10);
    heap.insert(9);
    heap.insert(1);
    heap.insert(9);
    heap.insert(9);
    heap.insert(5);

    heap.delete();
    expect(heap.getMax()).toEqual(9);
  });

  it('should delete the elements from greatest to least', () => {
    heap.insert(6);
    heap.insert(7);
    heap.insert(5);
    heap.insert(8);
    heap.insert(10);
    console.log(heap.storage);
    heap.insert(1);
    heap.insert(2);
    heap.insert(5);

    const descendingOrder = [];
    while (heap.getSize() > 0) {
      descendingOrder.push(heap.delete());
    }

    expect(descendingOrder).toEqual([10, 8, 7, 6, 5, 5, 2, 1]);
  });
});