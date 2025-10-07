/*
Problem: Implement Queue using Stacks

Description:
Implement a first-in-first-out (FIFO) queue using only two stacks. 
The implemented queue should support the following operations:
- push(x): Push element x to the back of the queue.
- pop(): Removes the element from the front of the queue and returns it.
- peek(): Returns the element at the front of the queue.
- empty(): Returns true if the queue is empty, false otherwise.

Example:
MyQueue queue = new MyQueue();
queue.push(1);
queue.push(2);
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false

Constraints:
- 1 <= number of operations <= 100
- For each call to push, 1 <= x <= 9
*/

import java.util.Stack;

class MyQueue {
    private Stack<Integer> inputStack;  // Stack used for enqueue operations
    private Stack<Integer> outputStack; // Stack used for dequeue operations

    /** Initialize your data structure here. */
    public MyQueue() {
        inputStack = new Stack<>();
        outputStack = new Stack<>();
    }

    /** Push element x to the back of queue. */
    public void push(int x) {
        inputStack.push(x);
    }

    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        shiftStacks(); // Ensure outputStack has the current front element
        return outputStack.pop();
    }

    /** Get the front element. */
    public int peek() {
        shiftStacks();
        return outputStack.peek();
    }

    /** Returns whether the queue is empty. */
    public boolean empty() {
        return inputStack.isEmpty() && outputStack.isEmpty();
    }

    /**
     * Helper function to transfer elements from inputStack to outputStack
     * only when outputStack is empty.
     * This ensures the correct FIFO order for pop/peek operations.
     */
    private void shiftStacks() {
        if (outputStack.isEmpty()) {
            while (!inputStack.isEmpty()) {
                outputStack.push(inputStack.pop());
            }
        }
    }
}

/*
Approach:
We use two stacks to simulate a queue:
- inputStack: stores new elements pushed to the back of the queue.
- outputStack: used for popping and peeking elements in correct order.

The trick is to move all elements from inputStack to outputStack only when needed.
When outputStack is empty, transfer all items from inputStack (reversing their order).
This ensures that the oldest element (FIFO order) appears at the top of outputStack.

Steps:
1. push(x): Push x to inputStack.
2. pop(): If outputStack is empty, move all elements from inputStack to outputStack.
          Then pop from outputStack.
3. peek(): Same as pop, but return the top instead of removing it.
4. empty(): Return true if both stacks are empty.

Time and Space Complexity:
- Amortized Time Complexity:
  - push: O(1)
  - pop: O(1)
  - peek: O(1)
  - empty: O(1)
  (Each element is moved between stacks at most once)
- Space Complexity: O(n)
  (n = total elements stored across both stacks)
*/
