const DoublyLinkedList = require('../src/doubly-linked-list');

let list;

describe('DoublyLinkedList', () => {
  beforeEach(() => {
    list = new DoublyLinkedList();
  });

  it('should have the methods "addToHead", "addToTail", "removeFromHead", "removeFromTail", "delete", "moveToFront", and "moveToBack"', () => {
    const hasAddToTail = Object.getPrototypeOf(list).hasOwnProperty('addToTail');
    const hasAddToHead = Object.getPrototypeOf(list).hasOwnProperty('addToHead');
    const hasRemoveFromHead = Object.getPrototypeOf(list).hasOwnProperty('removeFromHead');
    const hasRemoveFromTail = Object.getPrototypeOf(list).hasOwnProperty('removeFromTail');
    const hasMoveToFront = Object.getPrototypeOf(list).hasOwnProperty('moveToFront');
    const hasMoveToBack = Object.getPrototypeOf(list).hasOwnProperty('moveToBack');
    const hasDelete = Object.getPrototypeOf(list).hasOwnProperty('delete');
    expect(hasAddToHead).toBe(true);
    expect(hasAddToTail).toBe(true);
    expect(hasRemoveFromHead).toBe(true);
    expect(hasRemoveFromTail).toBe(true);
    expect(hasMoveToBack).toBe(true);
    expect(hasMoveToFront).toBe(true);
    expect(hasDelete).toBe(true);
  });

  it('should be able to add list nodes to the head of the list', () => {
    list.addToHead(1);
    list.addToHead(2);
    list.addToHead(3);
    expect(list.head.value).toEqual(3);
    expect(list.head.next.value).toEqual(2);
    expect(list.head.next.next.value).toEqual(1);
    expect(list.tail.value).toEqual(1);
  });

  it('should be able to add list nodes to the tail of the list', () => {
    list.addToTail(100);
    list.addToTail(99);
    list.addToTail(98);
    expect(list.head.value).toEqual(100);
    expect(list.tail.value).toEqual(98);
    expect(list.tail.prev.value).toEqual(99);
    expect(list.tail.prev.prev.value).toEqual(100);
  });

  it('should be able to remove the head node of the list', () => {
    list.addToHead(3);
    list.addToHead(39);
    expect(list.removeFromHead()).toEqual(39);
    expect(list.removeFromHead()).toEqual(3);
    expect(list.removeFromHead()).toBeNull();
    list.addToTail(18);
    expect(list.removeFromHead()).toEqual(18);
    expect(list.removeFromHead()).toBeNull();
  });

  it('should be able to remove the tail node of the list', () => {
    list.addToTail(18);
    list.addToTail(109);
    expect(list.removeFromTail()).toEqual(109);
    expect(list.removeFromTail()).toEqual(18);
    expect(list.removeFromTail()).toBeNull();
    list.addToHead(16);
    expect(list.removeFromTail()).toEqual(16);
    expect(list.removeFromTail()).toBeNull();
  });

  it('should be able to move an arbitrary node in the list to the front of the list', () => {
    list.addToTail(1);
    list.addToTail(10);
    list.addToTail(7);
    list.addToTail(3);
    expect(list.head.value).toEqual(1);
    expect(list.tail.value).toEqual(3);
    list.moveToFront(list.tail);
    expect(list.head.value).toEqual(3);
    expect(list.head.next.value).toEqual(1);
    expect(list.tail.value).toEqual(7);
    list.moveToFront(list.tail.prev);
    expect(list.head.value).toEqual(10);
  });

  it('should be able to move an arbitrary node in the list to the back of the list', () => {
    list.addToHead(1);
    list.addToHead(40);
    list.addToHead(29);
    list.addToHead(90);
    expect(list.tail.value).toEqual(1);
    expect(list.head.value).toEqual(90);
    list.moveToBack(list.head);
    console.log(list.tail)
    expect(list.tail.value).toEqual(90);
    expect(list.tail.prev.value).toEqual(1);
    list.moveToBack(list.head.next);
    expect(list.head.value).toEqual(29);
  });

  it('should be able to delete an arbitrary node in the list', () => {
    list.addToHead(8);
    list.addToHead(11);
    list.addToHead(90);
    expect(list.head.next.value).toEqual(11);
    expect(list.tail.prev.value).toEqual(11);
    list.delete(list.head.next);
    expect(list.head.next.value).toEqual(8);
    expect(list.tail.prev.value).toEqual(90);
  });
});