const BinarySearchTree = require("../src/binary-search-tree");

let binarySearchTree;

describe("BinarySearchTree", () => {
  beforeEach(() => {
    binarySearchTree = new BinarySearchTree(5);
  });

  it.skip('should have methods named "insert", "contains", "getMax", "depthFirstForEach", and "breadthFirstForEach"', () => {
    expect(
      Object.getPrototypeOf(binarySearchTree).hasOwnProperty("insert")
    ).toBe(true);
    expect(
      Object.getPrototypeOf(binarySearchTree).hasOwnProperty("contains")
    ).toBe(true);
    expect(
      Object.getPrototypeOf(binarySearchTree).hasOwnProperty("getMax")
    ).toBe(true);
    expect(
      Object.getPrototypeOf(binarySearchTree).hasOwnProperty(
        "depthFirstForEach"
      )
    ).toBe(true);
    expect(
      Object.getPrototypeOf(binarySearchTree).hasOwnProperty(
        "breadthFirstForEach"
      )
    ).toBe(true);
  });

  it.skip("should insert values at the correct location in the tree", () => {
    binarySearchTree.insert(2);
    binarySearchTree.insert(3);
    binarySearchTree.insert(7);
    binarySearchTree.insert(6);
    expect(binarySearchTree.left.right.value).toBe(3);
    expect(binarySearchTree.right.left.value).toBe(6);
  });

  it.skip('should have a working "contains" method', () => {
    binarySearchTree.insert(2);
    binarySearchTree.insert(3);
    binarySearchTree.insert(7);
    expect(binarySearchTree.contains(7)).toBe(true);
    expect(binarySearchTree.contains(8)).toBe(false);
  });

  it.skip("should fetch the correct maximum value", () => {
    expect(binarySearchTree.getMax()).toBe(5);
    binarySearchTree.insert(30);
    expect(binarySearchTree.getMax()).toBe(30);
    binarySearchTree.insert(300);
    binarySearchTree.insert(3);
    expect(binarySearchTree.getMax()).toBe(300);
  });

  it.skip('should execute a callback on every value in a tree using "depthFirstForEach" in the correct order', () => {
    const array = [];
    const foo = value => array.push(value);
    binarySearchTree.insert(2);
    binarySearchTree.insert(3);
    binarySearchTree.insert(7);
    binarySearchTree.insert(9);
    binarySearchTree.depthFirstForEach(foo);
    expect(array).toEqual([5, 2, 3, 7, 9]);
  });

  it.skip('should execute a callback on every value in the tree using "breadthFirstForEach" in the correct order', () => {
    const array = [];
    const foo = value => array.push(value);
    binarySearchTree.insert(3);
    binarySearchTree.insert(4);
    binarySearchTree.insert(10);
    binarySearchTree.insert(9);
    binarySearchTree.insert(11);
    binarySearchTree.breadthFirstForEach(foo);
    expect(array).toEqual([5, 3, 10, 4, 9, 11]);
  });
});
