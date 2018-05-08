class BinarySearchTree {
    /* Do not modify the constructor */
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }

    /* Inserts the given value
  Make sure the rules of a binary search
  tree are being adhered to */
    insert(value) {
        const newNode = new BinarySearchTree(value);
        // add to left side if less than root
        if (value < this.value) {
            if (!this.left) {
                this.left = newNode;
            } else {
                this.left.insert(value);
            }
        }
        // add to right side if greater than root
        if (value >= this.value) {
            if (!this.right) {
                this.right = newNode;
            } else {
                this.right.insert(value);
            }
        }
    }

    /* Traverses the tree until either the
  target value has been found in the true
  or the entire tree has been searched.
  Returns true or false accordingly */
    contains(target) {
        // capture all the node in a variable
        // set a flag to false
        let currentNode = this;
        let found = false;
        // while found is false and currNode is not null
        while (!found && currentNode) {
            // if target is less than value at current node set current node to the left side to check that side
            if (target < currentNode.value) {
                currentNode = currentNode.left;
                // if target is greater than current node set it val to the right side to check that side
            } else if (target > currentNode.value) {
                currentNode = currentNode.right;
                // if target equals the current nodes value then set flag to true
            } else {
                found = true;
            }
        }
        return found;
    }

    /* Returns the maximum value in the tree 
  Should not remove the max value from the tree */
    getMax() {
        // set value to max
        let max = this.value;
        // capture the tree so you can get the right side
        let currentNode = this;
        // while there is a right side set node to it
        // set max to the value
        while (currentNode.right) {
            currentNode = currentNode.right;
            max = currentNode.value;
        }
        //return the max
        return max;
    }

    /* Traverses the tree in a 'vertical' fashion,
  from parent to child. Executes the given callback
  on each visited tree node */
    depthFirstForEach(cb) {}

    /* Traverses the tree in a 'horizontal' fashion,
  from sibling to sibling. Executes the given callback
  on each visited tree node */
    breadthFirstForEach(cb) {}
}

const newTree = new BinarySearchTree(10);
newTree.insert(3);
newTree.insert(30);
newTree.insert(6);
newTree.insert(11);
newTree.insert(1);
newTree.insert(45);

// console.log("MAXXXXXX", newTree.getMax());
console.log("+++++++++", newTree);
console.log("CONTAINSSSSS", newTree.contains(111));

module.exports = BinarySearchTree;
