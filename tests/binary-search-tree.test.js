const BinarySearchTree = require('../src/binary-search-tree');

let binarySearchTree;

describe('BinarySearchTree', () => {
	beforeEach(() => {
		binarySearchTree = new BinarySearchTree(5);
	});

	it('should have methods named "insert", "contains", "getMax", "depthFirstForEach", and "breadthFirstForEach"', () => {
		expect(
			Object.getPrototypeOf(binarySearchTree).hasOwnProperty('insert'),
		).toBe(true);
		expect(
			Object.getPrototypeOf(binarySearchTree).hasOwnProperty('contains'),
		).toBe(true);
		expect(
			Object.getPrototypeOf(binarySearchTree).hasOwnProperty('getMax'),
		).toBe(true);
		expect(
			Object.getPrototypeOf(binarySearchTree).hasOwnProperty(
				'depthFirstForEach',
			),
		).toBe(true);
		expect(
			Object.getPrototypeOf(binarySearchTree).hasOwnProperty(
				'breadthFirstForEach',
			),
		).toBe(true);
	});

	it('should insert values at the correct location in the tree', () => {
		binarySearchTree.insert(2);
		binarySearchTree.insert(3);
		binarySearchTree.insert(7);
		binarySearchTree.insert(6);
		expect(binarySearchTree.left.right.value).toBe(3);
		expect(binarySearchTree.right.left.value).toBe(6);
	});

	it('should have a working "contains" method', () => {
		binarySearchTree.insert(2);
		binarySearchTree.insert(3);
		binarySearchTree.insert(7);
		expect(binarySearchTree.contains(7)).toBe(true);
		expect(binarySearchTree.contains(8)).toBe(false);
	});

	it('should fetch the correct maximum value', () => {
		expect(binarySearchTree.getMax()).toBe(5);
		binarySearchTree.insert(30);
		expect(binarySearchTree.getMax()).toBe(30);
		binarySearchTree.insert(300);
		binarySearchTree.insert(3);
		expect(binarySearchTree.getMax()).toBe(300);
	});
});
