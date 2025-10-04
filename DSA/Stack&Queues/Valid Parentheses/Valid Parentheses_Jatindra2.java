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
