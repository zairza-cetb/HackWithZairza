# Valid Parenthesis String
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:</br>
Any left parenthesis '(' must have a corresponding right parenthesis ')'.</br>
Any right parenthesis ')' must have a corresponding left parenthesis '('.</br>
Left parenthesis '(' must go before the corresponding right parenthesis ')'.</br>
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
</br>
### Example 1:
```
Input: s = "()"
Output: true
```
### Example 2:
```
Input: s = "(*)"
Output: true
```
### Example 3:
```
Input: s = "(*))"
Output: true
```

### Constraints:
* ```1 <= s.length <= 100```
* ```s[i] is '(', ')' or '*'```