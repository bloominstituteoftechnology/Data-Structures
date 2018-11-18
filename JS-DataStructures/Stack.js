class Stack {
    constructor() {
        this.storage = []
    }

    // Push item to top(last) of storage for LIFO behaviour
    push(item) {
        this.storage.push(item);
    }

    // Pop off top item in storage for LIFO behaviour -- This is "taking off the top plate"
    pop() {
        this.storage.pop()
    }

    peek() {
        return this.storage[this.storage.length - 1]
    }

    // Verify if stack is empty
    isEmpty() {
        if(!this.storage || this.storage.length < 1) {
            return true
        } else {
            return false
        }
    }

    // It's common to have a length function
    length()  {
        return this.storage.length
    }

    // Delete all items from the stack
    clearAll() {
        // O(n) solution...
        // while(this.storage.length > 0) {
        //     this.storage.pop()
        // }
        // O(1) solution...
        this.storage = []
    }

    print() {
        console.log("Stack: " + this.storage.toString());
    }
}

stack = new Stack();
stack.push("Brian")
stack.push("Shawn")
console.log(stack.length())
console.log(stack.isEmpty())
console.log(stack)
// stack.clearAll()
console.log(stack)
stack.print()
