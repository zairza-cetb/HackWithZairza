/*
Problem: Valid Parentheses

Describtion:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.


Approach:
To check if a string with brackets is valid, we use a stack. This is because brackets must be closed in the reverse order they are opened and a stack helps us track that.
Steps:
1. Create an empty stack to store opening brackets '(', '{', '['.
2. Iterate Through the String:
    - For each character:
        - If it is an opening bracket ('(', '{', '['), push it onto the stack.
        - If it is a closing bracket (')', '}', ']'):
            - Check if the stack is empty. If so, the string is invalid (no corresponding opening bracket).
            - Pop the top item from the stack.
            - Check if it matches the correct type of opening bracket:
                - For example, ) should match (, } should match {, etc.
                - If not, return false.
3. Final Validation:
    - After processing all characters, the stack should be empty if all brackets were correctly matched and closed.
    - If not, return false.


Time and Space Complexity:
    - Time Complexity: O(n) — each character is processed exactly once.
    - Space Complexity: O(n) — in the worst case, the stack holds all opening brackets.
    
*/

import java.util.*;
class Solution {
    public boolean isValid(String s) {
        // Created a Stack to store opening brackets
        Stack<Character> brackets = new Stack<>();
        int len = s.length();  // Length of String s

        // Traversed each Character of input String s
        for(int i = 0; i<len; i++){
            char ch = s.charAt(i); // Character at index i
            
            // If current Character is an opening bracket, store it in the Stack
            if(ch == '(' || ch == '{' || ch == '['){
                brackets.push(ch);
            }else{
                // If current Character is a closing bracket but Stack is empty, then it is an invalid Parentheses
                if(brackets.isEmpty()){
                    return false; 
                }

                char c = brackets.pop();  // Pop the top Character from the Stack
                // If current Character's appropriate closing bracket does not matches with the poped Character, then it is an invalid Parentheses
                if((ch == ')' && c != '(') || (ch == '}' && c != '{') || (ch == ']' && c != '[')){
                    return false;
                }
            }
        }
        // If the Stack is empty, all brackets were matched
        return brackets.isEmpty();
    }
}

// As we visited each Character exactly once during the iteration, so time complexity is O(n)
