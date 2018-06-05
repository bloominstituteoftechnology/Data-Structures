const LinkedList = require("../src/linked-list");

let list;

describe("LinkedList", () => {
  beforeEach(() => {
    list = new LinkedList();
  });

  it('should have the methods "addToTail", "removeHead", "getMax" and "contains"', () => {
    expect(Object.getPrototypeOf(list).hasOwnProperty("addToTail")).toBe(true);
    expect(Object.getPrototypeOf(list).hasOwnProperty("removeHead")).toBe(true);
    expect(Object.getPrototypeOf(list).hasOwnProperty("contains")).toBe(true);
    expect(Object.getPrototypeOf(list).hasOwnProperty("getMax")).toBe(true);
  });

  it("should update the tail value when a new node is added", () => {
    list.addToTail(1);
    expect(list.tail.value).toBe(1);
    list.addToTail(2);
    expect(list.tail.value).toBe(2);
  });

  it("should keep the same head after adding nodes", () => {
    list.addToTail(1);
    expect(list.head.value).toBe(1);
    list.addToTail(2);
    expect(list.head.value).toBe(1);
  });

  it("should return true from contains if a matching value is found and false otherwise", () => {
    list.addToTail(1);
    list.addToTail(2);
    list.addToTail(5);
    list.addToTail(10);
    expect(list.contains(10)).toBe(true);
    expect(list.contains("asdf")).toBe(false);
  });

  it('should remove head when "removeHead" is invoked', () => {
    list.addToTail(1);
    list.addToTail(2);
    expect(list.head.value).toBe(1);
    list.removeHead();
    expect(list.head.value).toBe(2);
    list.removeHead();
    expect(list.head).toBe(null);
  });

  it('should return the head that is removed when "removeHead" is invoked', () => {
    list.addToTail(1);
    expect(list.removeHead()).toBe(1);
  });

  it("should not contain removed values", () => {
    list.addToTail(1);
    list.addToTail(2);
    list.addToTail(3);
    list.addToTail(4);
    list.removeHead();
    expect(list.contains(1)).toBe(false);
  });

  it('should have a working "getMax" method', () => {
    expect(list.getMax()).toBeNull();
    list.addToTail(10);
    expect(list.getMax()).toBe(10);
    list.addToTail(1);
    list.addToTail(100);
    expect(list.getMax()).toBe(100);
  });
});
