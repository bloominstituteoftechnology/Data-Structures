class LinkedList {
    /* Do not modify the constructor */
    constructor() {
        this.head = null;
        this.tail = null;
        this.max = 0;
    }

    /* Add the given value to the tail
    of the list. The `tail` pointer
    should be updated accordingly */
    addToTail(value) {

        const newNode = {
            value,
            next: null
        };

        if(!this.head) {
            this.head = newNode;
            this.tail = newNode;
            this.max = value;
            return;
        }

        this.tail.next = newNode;
        this.tail = newNode;
       if (value > this.max) this.max = value;

    }

    /* Remove the list's `head` value
    The `head` pointer should be updated
    accordingly */
    removeHead() {
    }

    /* Searches the list for the given value
    Returns true or false accordingly */
    contains(value) {
        let currentNode = this.head;

        while(currentNode) {
            if(currentNode.value === value) return true;
            currentNode = currentNode.next;
        }
        return false;
    }

    /* Finds and returns the maximal value
    of all the values in the list */
    getMax() {
        return this.max;
    }
}

module.exports = LinkedList;