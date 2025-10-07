
/**
 * Author: DearAsutosh
 * Problem: Decode String (LeetCode #394)
 * Description: Decode an encoded string using stack-based approach
 *              following the rule k[encoded_string], where the string inside
 *              brackets is repeated exactly k times.
 */

import java.util.Stack;

public class DecodeString_DearAsutosh {

    public static String decodeString(String s) {

        // stack to store repetition counts
        Stack<Integer> countStack = new Stack<>();

        // Stack to store previous strings before a '['
        Stack<StringBuilder> stringStack = new Stack<>();

        // I prefer StringBuilder because of String mutability
        StringBuilder current = new StringBuilder();

        // Current repetition count
        int k = 0;

        // Traverse every character in the input string
        for (char ch : s.toCharArray()) {

            if (Character.isDigit(ch)) {

                // Build the repetition count (handles multiple digits)
                k = k * 10 + (ch - '0');

            } else if (ch == '[') {

                // push current count and string onto their respective stacks
                countStack.push(k);
                stringStack.push(current);

                // reset current string and start counting for new context
                current = new StringBuilder();
                k = 0;

            } else if (ch == ']') {
                // pop last added string and repetition count
                StringBuilder decoded = stringStack.pop();
                int count = countStack.pop();

                // append current string to the previous string 'count' times
                for (int i = 0; i < count; i++) {
                    decoded.append(current);
                }

                // Update current string
                current = decoded;

            } else {
                // append normal characters to current string
                // ONLY IF there is no any integer available in given string
                current.append(ch);
            }
        }

        // return fully decoded string
        return current.toString();
    }

    public static void main(String[] args) {
        String s1 = "3[a]2[bc]";
        String s2 = "3[a2[c]]";
        System.out.println("Decoded string of '" + s1 + "' : " + decodeString(s1));
        System.out.println("Decoded string of '" + s2 + "' : " + decodeString(s2));
    }
}
