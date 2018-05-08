class LinkedList {
    /* Do not modify the constructor */
    constructor() {
        this.head = null;
        this.tail = null;
    }

    /* Add the given value to the tail
  of the list. The `tail` pointer
  should be updated accordingly */
    addToTail(value) {
        // use value to create new node
        const newNode = {
            next: null,
            value: value,
        };

        // check to see if head is null
        if (this.head === null) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            // change the old tail to point to our new node
            this.tail.next = newNode;
            //update `this.tail` to point to our new node
            this.tail = newNode;
        }

    }

    /* Remove the list's `head` value 
  The `head` pointer should be updated
  accordingly */
    removeHead() {
        const value = this.head.value;
        this.head = this.head.next;
        return value;
    }

    /* Searches the list for the given value Returns true or false accordingly */
    contains(value) {
        let thisNode = this.head;

        while (thisNode) {
            if (thisNode.value === value) {
                return true;
            }
            thisNode = thisNode.next;
        }
        return false;
    }

    /* Finds and returns the maximal value
  of all the values in the list */
    getMax() {
        let max = null;
        let currentNode = this.head;

        // if (this.head === null) return null;

        while (currentNode) {
            if (currentNode.value > max) max = currentNode.value;
            currentNode = currentNode.next;
        }
        return max;
    }
}

module.exports = LinkedList;