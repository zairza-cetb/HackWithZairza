# Level 1: Password Tools

Create password security utilities for checking password strength and generating secure passwords. Focus on understanding password security fundamentals and entropy.

## Project Options

### Option 1: Password Strength Checker
Tool to evaluate password security based on various criteria.

**Features:**
- Check password length
- Evaluate character diversity (uppercase, lowercase, numbers, symbols)
- Calculate entropy score
- Check against common password lists
- Provide strength rating (weak, medium, strong)
- Suggest improvements

### Option 2: Secure Password Generator
Generate cryptographically secure random passwords.

**Features:**
- Customizable length
- Character set options (letters, numbers, symbols)
- Exclude ambiguous characters option
- Multiple password generation
- Entropy calculation
- Copy to clipboard functionality

### Option 3: Password Policy Validator
Validate passwords against organizational security policies.

**Features:**
- Configurable policy rules
- Minimum length requirements
- Character class requirements
- Dictionary word detection
- Pattern detection (repeated characters, sequences)
- Compliance reporting

## Implementation Example
```
import string
import secrets
import re
from math import log2

def calculate_entropy(password):
"""Calculate password entropy in bits"""
charset_size = 0

text
if any(c.islower() for c in password):
    charset_size += 26
if any(c.isupper() for c in password):
    charset_size += 26
if any(c.isdigit() for c in password):
    charset_size += 10
if any(c in string.punctuation for c in password):
    charset_size += len(string.punctuation)

if charset_size == 0:
    return 0

entropy = len(password) * log2(charset_size)
return round(entropy, 2)
def check_password_strength(password):
"""Evaluate password strength"""
score = 0
feedback = []

text
# Length check
if len(password) >= 12:
    score += 2
elif len(password) >= 8:
    score += 1
else:
    feedback.append("Password should be at least 8 characters")

# Character diversity
if any(c.islower() for c in password):
    score += 1
else:
    feedback.append("Add lowercase letters")

if any(c.isupper() for c in password):
    score += 1
else:
    feedback.append("Add uppercase letters")

if any(c.isdigit() for c in password):
    score += 1
else:
    feedback.append("Add numbers")

if any(c in string.punctuation for c in password):
    score += 1
else:
    feedback.append("Add special characters")

# Pattern checks
if re.search(r'(.)\1{2,}', password):
    score -= 1
    feedback.append("Avoid repeated characters")

if re.search(r'(012|123|234|345|456|567|678|789|890|abc|bcd|cde)', password.lower()):
    score -= 1
    feedback.append("Avoid sequential patterns")

# Determine strength
entropy = calculate_entropy(password)

if score >= 6 and entropy >= 60:
    strength = "Strong"
elif score >= 4 and entropy >= 40:
    strength = "Medium"
else:
    strength = "Weak"

return {
    'strength': strength,
    'score': score,
    'entropy': entropy,
    'feedback': feedback
}
def generate_secure_password(length=16, use_symbols=True):
"""Generate cryptographically secure password"""
if length < 8:
raise ValueError("Password length should be at least 8 characters")

text
# Character sets
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation if use_symbols else ''

# Build character pool
all_chars = lowercase + uppercase + digits + symbols

# Ensure at least one character from each category
password = [
    secrets.choice(lowercase),
    secrets.choice(uppercase),
    secrets.choice(digits)
]

if use_symbols:
    password.append(secrets.choice(symbols))

# Fill remaining length
password += [secrets.choice(all_chars) for _ in range(length - len(password))]

# Shuffle to randomize positions
secrets.SystemRandom().shuffle(password)

return ''.join(password)
# Example usage
if name == "main":
# Check password strength
test_password = "MyP@ssw0rd123"
result = check_password_strength(test_password)
print(f"Password: {test_password}")
print(f"Strength: {result['strength']}")
print(f"Entropy: {result['entropy']} bits")
print(f"Feedback: {', '.join(result['feedback'])}")

text
# Generate secure password
new_password = generate_secure_password(16)
print(f"\nGenerated Password: {new_password}")
print(f"Entropy: {calculate_entropy(new_password)} bits")
```


## Technical Requirements

1. **Secure random generation** using secrets module
2. **Entropy calculation** for password strength
3. **Pattern detection** for common weaknesses
4. **Character diversity validation**
5. **User-friendly feedback** system

## Security Best Practices

- Use `secrets` module, not `random`, for password generation
- Never store passwords in plain text
- Implement proper entropy calculations
- Check against known breach databases (optional)
- Provide educational feedback to users

## Dependencies
```
# No external dependencies for basic implementation
# Optional:
# requests>=2.31.0 # For breach database API
```


## Submission Requirements

Folder `PasswordTool_YourGitHubUsername` containing:

1. `password_tool.py` - Main implementation
2. `README.md` - Documentation with:
   - Tool description
   - Usage examples
   - Security considerations
   - Entropy calculation explanation
3. `requirements.txt` - Dependencies (if any)
4. `tests/` - Unit tests (optional)

## Resources

- [NIST Password Guidelines](https://pages.nist.gov/800-63-3/sp800-63b.html)
- [Python Secrets Module](https://docs.python.org/3/library/secrets.html)
- [Password Entropy](https://en.wikipedia.org/wiki/Password_strength)
- [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

