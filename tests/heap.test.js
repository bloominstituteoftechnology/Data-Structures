const sinon = require('sinon');
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
    heap.insert(1);
    heap.insert(2);
    heap.insert(5);

    const descendingOrder = [];
    while (heap.getSize() > 0) {
      descendingOrder.push(heap.delete());
    }

    expect(descendingOrder).toEqual([10, 8, 7, 6, 5, 5, 2, 1]);
  });

  test('insert method calls the bubbleUp method', () => {
    const spy = sinon.spy(heap, 'bubbleUp');

    heap.insert(0);

    expect(spy.called).toBe(true);
  });

  test('delete method calls the siftDown method when heap has two or more elements', () => {
    const spy = sinon.spy(heap, 'siftDown');

    heap.insert(10);
    heap.insert(12);
    heap.delete()

    expect(spy.called).toBe(true);
  });

  test('bubbleUp moves the value at the specified index up to its correct spot in the heap', () => {
    heap.storage = [100, 19, 36, 17, 3, 25, 1, 2, 7, 20];
    heap.bubbleUp(9);

    expect(heap.storage).toEqual([100, 20, 36, 17, 19, 25, 1, 2, 7, 3]);
  });

  test('siftDown moves the element at the specified index down to its correct spot in the heap', () => {
    heap.storage = [7, 19, 36, 17, 3, 25, 1, 2];
    heap.siftDown(0);

    expect(heap.storage).toEqual([36, 19, 25, 17, 3, 7, 1, 2]);
  });
})