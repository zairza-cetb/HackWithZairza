# Level 3: Vulnerability Demos

Educational demonstrations of common web vulnerabilities in controlled environments. Understand attack vectors to build better defenses.

## **CRITICAL ETHICAL WARNING**

These demonstrations are for EDUCATIONAL PURPOSES ONLY.

**Legal Requirements:**
- Only test on systems you own or have written permission to test
- Never use these techniques on production systems
- Unauthorized access is ILLEGAL and punishable by law
- These tools are for learning defense strategies

## Project Options

### Option 1: XSS Vulnerability Demonstrator
Educational tool showing Cross-Site Scripting (XSS) vulnerabilities.

**Features:**
- Vulnerable web form demo
- Different XSS types (Stored, Reflected, DOM-based)
- Safe payload examples
- Mitigation strategies demonstration
- Input sanitization examples

### Option 2: SQL Injection Educational Demo
Demonstrate SQL injection vulnerabilities in controlled environment.

**Features:**
- Vulnerable login form
- SQL injection examples
- Parameterized query comparison
- Input validation demonstrations
- Prevention techniques

### Option 3: Security Vulnerability Scanner
Educational tool to identify common security issues.

**Features:**
- Check for insecure configurations
- Identify missing security headers
- Detect common vulnerabilities
- Generate security report
- Provide remediation guidance

## Implementation Example
```
from flask import Flask, request, render_template_string
import sqlite3

app = Flask(name)

# VULNERABLE CODE - FOR EDUCATIONAL PURPOSES ONLY
@app.route('/vulnerable-login', methods=['GET', 'POST'])
def vulnerable_login():
"""
EDUCATIONAL DEMO: SQL Injection Vulnerability
WARNING: Never use this pattern in production!
"""
if request.method == 'POST':
username = request.form['username']
password = request.form['password']

text
    # VULNERABLE: String concatenation in SQL query
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    # Create demo table
    cursor.execute('CREATE TABLE users (username TEXT, password TEXT)')
    cursor.execute("INSERT INTO users VALUES ('admin', 'secret123')")
    
    try:
        cursor.execute(query)
        result = cursor.fetchone()
        
        if result:
            return f"""
            <h2 style='color: red;'>⚠️ VULNERABLE: Login Successful!</h2>
            <p>Query executed: <code>{query}</code></p>
            <p>This demonstrates SQL injection vulnerability.</p>
            <p><strong>Try:</strong> username: admin' OR '1'='1</p>
            """
        else:
            return "Login failed"
    except Exception as e:
        return f"Error: {str(e)}"

return '''
    <h2>SQL Injection Demo (EDUCATIONAL)</h2>
    <form method="POST">
        Username: <input name="username"><br>
        Password: <input name="password" type="password"><br>
        <input type="submit" value="Login">
    </form>
    <p><em>WARNING: This is a deliberately vulnerable demo!</em></p>
'''
# SECURE CODE - Proper Implementation
@app.route('/secure-login', methods=['GET', 'POST'])
def secure_login():
"""
SECURE IMPLEMENTATION: Using parameterized queries
"""
if request.method == 'POST':
username = request.form['username']
password = request.form['password']

text
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    # Create demo table
    cursor.execute('CREATE TABLE users (username TEXT, password TEXT)')
    cursor.execute("INSERT INTO users VALUES ('admin', 'secret123')")
    
    # SECURE: Parameterized query
    query = "SELECT * FROM users WHERE username=? AND password=?"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    
    if result:
        return """
        <h2 style='color: green;'>✓ SECURE: Login Successful</h2>
        <p>This implementation uses parameterized queries.</p>
        <p>SQL injection attempts will fail safely.</p>
        """
    else:
        return "Login failed"

return '''
    <h2>Secure Login Demo</h2>
    <form method="POST">
        Username: <input name="username"><br>
        Password: <input name="password" type="password"><br>
        <input type="submit" value="Login">
    </form>
    <p><em>This implementation is protected against SQL injection.</em></p>
'''
### XSS Vulnerability Demo
@app.route('/vulnerable-comment', methods=['GET', 'POST'])
def vulnerable_comment():
"""
EDUCATIONAL DEMO: XSS Vulnerability
WARNING: Never use this pattern in production!
"""
if request.method == 'POST':
comment = request.form['comment']

text
    # VULNERABLE: Direct rendering without escaping
    return f"""
    <h2 style='color: red;'>⚠️ VULNERABLE: Comment Posted</h2>
    <div style='border: 1px solid red; padding: 10px;'>
        {comment}
    </div>
    <p><strong>Try:</strong> &lt;script&gt;alert('XSS')&lt;/script&gt;</p>
    <a href='/vulnerable-comment'>Back</a>
    """

return '''
    <h2>XSS Demo (EDUCATIONAL)</h2>
    <form method="POST">
        Comment: <textarea name="comment"></textarea><br>
        <input type="submit" value="Post">
    </form>
    <p><em>WARNING: This is deliberately vulnerable to XSS!</em></p>
'''
# Security Headers Checker
def check_security_headers(url):
"""Check for important security headers"""
import requests

text
try:
    response = requests.get(url, timeout=5)
    headers = response.headers
    
    security_headers = {
        'X-Content-Type-Options': 'nosniff',
        'X-Frame-Options': 'DENY or SAMEORIGIN',
        'X-XSS-Protection': '1; mode=block',
        'Strict-Transport-Security': 'max-age=31536000',
        'Content-Security-Policy': 'CSP policy'
    }
    
    report = []
    for header, expected in security_headers.items():
        if header in headers:
            report.append(f"✓ {header}: {headers[header]}")
        else:
            report.append(f"✗ Missing: {header} (Expected: {expected})")
    
    return '\n'.join(report)
except Exception as e:
    return f"Error checking headers: {e}"
if name == "main":
print("=" * 60)
print("EDUCATIONAL SECURITY DEMO")
print("WARNING: For learning purposes only!")
print("=" * 60)
app.run(debug=True, host='127.0.0.1', port=5000)
```


## Technical Requirements

1. **Isolated testing environment** only
2. **Clear vulnerability explanations**
3. **Side-by-side secure vs insecure code**
4. **Mitigation strategies documented**
5. **Ethical warnings** throughout code

## Ethical Guidelines

**Before implementing:**
- Set up isolated local environment
- Never deploy to public servers
- Include prominent warnings
- Document educational purpose
- Provide secure alternatives

**Demonstration scope:**
- Local testing only
- Controlled environments
- Clear educational intent
- No malicious payloads
- Focus on defense strategies

## Dependencies
```
flask>=3.0.0
requests>=2.31.0
```


## Submission Requirements

Folder `VulnerabilityDemo_YourGitHubUsername` containing:

1. `demo_app.py` - Demo application
2. `README.md` - Documentation with:
   - Vulnerability explanations
   - Ethical warnings (prominent)
   - Setup instructions
   - Mitigation strategies
   - References to OWASP resources
3. `requirements.txt` - Dependencies
4. `SECURITY.md` - Ethical use policy

## Documentation Requirements

Each demo MUST include:
- Description of vulnerability
- How it works technically
- Real-world impact examples
- Proper mitigation techniques
- Secure code alternatives
- OWASP references

## Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- [OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)
