/*
Problem: Implement Queue using Stacks

Description:
  Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
  Implement the MyQueue class:
    - void push(int x) Pushes element x to the back of the queue.
    - int pop() Removes the element from the front of the queue and returns it.
    - int peek() Returns the element at the front of the queue.
    - boolean empty() Returns true if the queue is empty, false otherwise.

Approach:
  Stacks follow LIFO (Last-In-First-Out) order, while queues follow FIFO (First-In-First-Out). To implement a queue using stacks, we need to reverse the order of elements so that the first pushed element is the first to be popped.
  We can achieve this using two stacks:
    - One for input (stack1), where we store elements in the order they arrive.
    - One for output (stack2), from which we retrieve elements in the correct queue order.
  The move() method transfers elements from stack1 to stack2 only when stack2 is empty. This reverses the order, so the oldest element (first pushed) ends up on top of stack2.
  Steps for Each Operation:
    1. push(int x)
      - Directly push the element onto stack1.
    2. pop()
      - If stack2 is empty, move all elements from stack1 to stack2.
      - Then pop from stack2.
    3. peek()
      - If stack2 is empty, move all elements from stack1 to stack2.
      - Then return the top of stack2.
    4. empty()
      - Return true if both stack1 and stack2 are empty.

Time Complexity:
  push(x): O(1)   - Direct push to `stack1`.
  pop(): Average O(1), Worst O(n)   - Transfers elements only if `stack2` is empty. Each element moves at most once from `stack1` to `stack2
  peek(): Average O(1), Worst O(n)  - Same logic as `pop()`, but doesn't remove the element.
  empty(): O(1)   - Checks if both stacks are empty.
Space Complexity: O(n) - at most n elements are stored between the two stacks.

Example:
  Operation	stack1	stack2	Output
  MyQueue q = new MyQueue();
  q.push(10)	    stack1: [10]	     stack2: []	
  q.push(20)	    stack1 [10, 20]	   stack2: []	
  q.peek()	      stack1: []	       stack2: [20, 10]	   return: 10
  q.pop()	        stack1: []	       stack2: [20]	       return: 10
  q.pop()	        stack1: []	       stack2: []        return: 20
  q.empty()	      stack1: []	       stack2: []	         return: true

*/

class MyQueue {
    private Stack<Integer> stack1;
    private Stack<Integer> stack2;

    public MyQueue() {
        stack1 = new Stack<>();
        stack2 = new Stack<>();
    }
    
    public void push(int x) {
        stack1.push(x);
    }
    
    public int pop() {
        move();
        return stack2.pop();
    }
    
    public int peek() {
        move();
        return stack2.peek();
    }
    
    public boolean empty() {
        return stack1.empty() && stack2.empty();
    }

    public void move(){
        if(stack2.empty()){
            while(!stack1.empty()){
                stack2.push(stack1.pop());
            }
        }
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
