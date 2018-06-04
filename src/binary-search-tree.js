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

        if (value > this.value) {
            if(!this.right) {
                this.right = new BinarySearchTree(value);
            }
            else {
                this.right.insert(value);
            }
        }

        else {
            if (!this.left) {
                this.left = new BinarySearchTree(value);
            }
            else {
                this.left.insert(value);
            }
        }
    }

    /* Traverses the tree until either the
    target value has been found in the true
    or the entire tree has been searched.
    Returns true or false accordingly */
    contains(target) {
        if (this.value === target) return true;
        if ( this.value > target) {
            if (this.left) {
                if (this.left.contains(target)) return true;
            }
        }
        else {
            if (this.right) {
                if (this.right.contains(target)) return true;
            }
        }
        return false;
    }


    /* Returns the maximum value in the tree
    Should not remove the max value from the tree */
    getMax() {

        // if left and right are null return root
        if (this.left === null && this.right === null) return this.value;
        // return the side
        else if (this.right) return this.right.getMax();
        // if right is null return left
        else return this.left.getMax();
    }

    depthFirstForEach(cb) {

    }

    breadthFirstForEach(cb) {

    }
}

module.exports = BinarySearchTree;