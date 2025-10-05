# Level 2: Basic Encryption/Decryption

Implement common encryption algorithms and ciphers to understand cryptographic fundamentals. Focus on educational implementations demonstrating encryption concepts.

## Project Options

### Option 1: Caesar Cipher Tool
Educational implementation of classical substitution cipher.

**Features:**
- Encrypt and decrypt text
- Configurable shift value
- Brute force decryption
- Frequency analysis
- Support for multiple languages

### Option 2: Modern Encryption Suite
Implement modern symmetric encryption algorithms.

**Features:**
- AES encryption/decryption
- Key generation and management
- File encryption support
- Password-based encryption
- Initialization vector (IV) handling

### Option 3: Hash Function Tool
Demonstrate various hashing algorithms and their uses.

**Features:**
- Multiple hash algorithms (MD5, SHA256, SHA512)
- File integrity verification
- Password hashing with salt
- Hash collision demonstration
- HMAC implementation

## Implementation Example
```
import hashlib
import secrets
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2

Caesar Cipher (Educational)
def caesar_encrypt(text, shift):
"""Classical Caesar cipher encryption"""
result = ""
for char in text:
if char.isalpha():
ascii_offset = 65 if char.isupper() else 97
result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
else:
result += char
return result

def caesar_decrypt(text, shift):
"""Caesar cipher decryption"""
return caesar_encrypt(text, -shift)

def caesar_brute_force(ciphertext):
"""Try all possible shifts"""
print("Brute force attempts:")
for shift in range(26):
decrypted = caesar_decrypt(ciphertext, shift)
print(f"Shift {shift}: {decrypted}")

Modern Encryption (AES via Fernet)
def generate_key():
"""Generate encryption key"""
return Fernet.generate_key()

def derive_key_from_password(password, salt=None):
"""Derive encryption key from password"""
if salt is None:
salt = secrets.token_bytes(16)

text
kdf = PBKDF2(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
)
key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
return key, salt
def encrypt_message(message, key):
"""Encrypt message with Fernet"""
f = Fernet(key)
encrypted = f.encrypt(message.encode())
return encrypted

def decrypt_message(encrypted_message, key):
"""Decrypt message with Fernet"""
f = Fernet(key)
try:
decrypted = f.decrypt(encrypted_message)
return decrypted.decode()
except:
return "Decryption failed - invalid key or corrupted data"

Hashing Functions
def hash_text(text, algorithm='sha256'):
"""Hash text using specified algorithm"""
if algorithm == 'md5':
h = hashlib.md5()
elif algorithm == 'sha1':
h = hashlib.sha1()
elif algorithm == 'sha256':
h = hashlib.sha256()
elif algorithm == 'sha512':
h = hashlib.sha512()
else:
raise ValueError("Unsupported algorithm")

text
h.update(text.encode())
return h.hexdigest()
def hash_password(password, salt=None):
"""Hash password with salt"""
if salt is None:
salt = secrets.token_hex(16)

text
# PBKDF2 for password hashing
key = hashlib.pbkdf2_hmac(
    'sha256',
    password.encode(),
    salt.encode(),
    100000
)
return f"{salt}${key.hex()}"
def verify_password(password, hashed):
"""Verify password against hash"""
salt, key = hashed.split('$')
new_hash = hash_password(password, salt)
return new_hash == hashed

def calculate_file_hash(filepath, algorithm='sha256'):
"""Calculate hash of file"""
if algorithm == 'sha256':
h = hashlib.sha256()
else:
h = hashlib.md5()

text
with open(filepath, 'rb') as f:
    while chunk := f.read(8192):
        h.update(chunk)

return h.hexdigest()
# Example usage
if name == "main":
# Caesar Cipher Demo
print("=== Caesar Cipher ===")
plaintext = "Hello World"
encrypted = caesar_encrypt(plaintext, 3)
print(f"Plaintext: {plaintext}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {caesar_decrypt(encrypted, 3)}\n")

text
# Modern Encryption Demo
print("=== AES Encryption (Fernet) ===")
key = generate_key()
message = "Sensitive information"
encrypted_msg = encrypt_message(message, key)
print(f"Original: {message}")
print(f"Encrypted: {encrypted_msg}")
print(f"Decrypted: {decrypt_message(encrypted_msg, key)}\n")

# Hashing Demo
print("=== Hashing ===")
text = "Password123"
print(f"MD5: {hash_text(text, 'md5')}")
print(f"SHA256: {hash_text(text, 'sha256')}")

# Password Hashing
hashed = hash_password("mypassword")
print(f"Hashed password: {hashed}")
print(f"Verification: {verify_password('mypassword', hashed)}")
```


## Technical Requirements

1. **Correct algorithm implementation**
2. **Secure key generation** using cryptographic libraries
3. **Proper error handling**
4. **Educational documentation** explaining concepts
5. **Security warnings** about usage

## Security Warnings

**IMPORTANT:**
- Caesar cipher is NOT secure for real use
- Never implement your own cryptographic algorithms for production
- Use established libraries (cryptography, PyCryptodome)
- MD5 and SHA1 are deprecated for security purposes
- Always use salt for password hashing

## Dependencies
```
cryptography>=41.0.0
```


## Submission Requirements

Folder `EncryptionTool_YourGitHubUsername` containing:

1. `crypto_tool.py` - Implementation
2. `README.md` - Documentation with:
   - Algorithm explanations
   - Security considerations
   - Usage examples
   - Educational warnings
3. `requirements.txt` - Dependencies
4. `examples/` - Sample encrypted files

## Resources

- [Python Cryptography Library](https://cryptography.io/)
- [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
- [Understanding Encryption](https://www.khanacademy.org/computing/computer-science/cryptography)
