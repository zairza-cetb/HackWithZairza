# Level 4: Security Audit Tools

Build comprehensive security assessment tools and checklists for identifying vulnerabilities and compliance issues. Focus on automated security auditing and reporting.

## Project Options

### Option 1: Web Application Security Scanner
Automated tool to scan web applications for common vulnerabilities.

**Features:**
- Security header analysis
- SSL/TLS configuration check
- Common vulnerability scanning (XSS, SQLi patterns)
- Directory enumeration
- Outdated software detection
- Comprehensive security report generation

### Option 2: Code Security Analyzer
Static analysis tool for identifying security issues in source code.

**Features:**
- Scan for hardcoded credentials
- Detect insecure functions
- Identify SQL injection vulnerabilities
- Check for weak cryptography
- OWASP compliance checking
- Generate detailed reports

### Option 3: Security Compliance Checker
Tool to verify security configurations against best practices.

**Features:**
- Check HTTPS configuration
- Validate security headers
- Test authentication mechanisms
- Verify file permissions
- Generate compliance reports
- Remediation recommendations

## Implementation Example
```
import requests
import ssl
import socket
from urllib.parse import urlparse
import re
from datetime import datetime

class SecurityAuditor:
"""Comprehensive security audit tool"""

text
def __init__(self, target_url):
    self.target = target_url
    self.parsed_url = urlparse(target_url)
    self.report = {
        'url': target_url,
        'scan_date': datetime.now().isoformat(),
        'findings': [],
        'security_score': 0
    }

def check_https(self):
    """Verify HTTPS configuration"""
    if self.parsed_url.scheme != 'https':
        self.report['findings'].append({
            'severity': 'HIGH',
            'category': 'Transport Security',
            'issue': 'Site not using HTTPS',
            'recommendation': 'Enable HTTPS with valid SSL certificate'
        })
        return False
    return True

def check_ssl_certificate(self):
    """Check SSL certificate validity"""
    try:
        hostname = self.parsed_url.netloc
        context = ssl.create_default_context()
        
        with socket.create_connection((hostname, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                
                # Check expiration
                not_after = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                days_until_expiry = (not_after - datetime.now()).days
                
                if days_until_expiry < 30:
                    self.report['findings'].append({
                        'severity': 'MEDIUM',
                        'category': 'Certificate',
                        'issue': f'Certificate expires in {days_until_expiry} days',
                        'recommendation': 'Renew SSL certificate soon'
                    })
        
        return True
    except Exception as e:
        self.report['findings'].append({
            'severity': 'HIGH',
            'category': 'Certificate',
            'issue': f'SSL certificate error: {str(e)}',
            'recommendation': 'Fix SSL certificate configuration'
        })
        return False

def check_security_headers(self):
    """Check for important security headers"""
    try:
        response = requests.get(self.target, timeout=10)
        headers = response.headers
        
        required_headers = {
            'Strict-Transport-Security': {
                'severity': 'HIGH',
                'description': 'HSTS header missing - site vulnerable to downgrade attacks'
            },
            'X-Content-Type-Options': {
                'severity': 'MEDIUM',
                'description': 'Content type sniffing not disabled'
            },
            'X-Frame-Options': {
                'severity': 'MEDIUM',
                'description': 'Clickjacking protection missing'
            },
            'Content-Security-Policy': {
                'severity': 'MEDIUM',
                'description': 'CSP not implemented - XSS protection limited'
            },
            'X-XSS-Protection': {
                'severity': 'LOW',
                'description': 'Legacy XSS protection header missing'
            }
        }
        
        for header, info in required_headers.items():
            if header not in headers:
                self.report['findings'].append({
                    'severity': info['severity'],
                    'category': 'Security Headers',
                    'issue': f'Missing {header} header',
                    'recommendation': info['description']
                })
        
    except Exception as e:
        self.report['findings'].append({
            'severity': 'HIGH',
            'category': 'Connection',
            'issue': f'Cannot connect to target: {str(e)}',
            'recommendation': 'Verify URL is accessible'
        })

def check_cookie_security(self):
    """Check cookie security attributes"""
    try:
        response = requests.get(self.target, timeout=10)
        cookies = response.cookies
        
        for cookie in cookies:
            issues = []
            
            if not cookie.secure:
                issues.append('Secure flag not set')
            
            if not cookie.has_nonstandard_attr('HttpOnly'):
                issues.append('HttpOnly flag not set')
            
            if not cookie.has_nonstandard_attr('SameSite'):
                issues.append('SameSite attribute not set')
            
            if issues:
                self.report['findings'].append({
                    'severity': 'MEDIUM',
                    'category': 'Cookie Security',
                    'issue': f'Cookie "{cookie.name}": {", ".join(issues)}',
                    'recommendation': 'Set secure cookie attributes'
                })
    
    except Exception:
        pass  # No cookies found

def scan_for_sensitive_data(self, response_text):
    """Scan for exposed sensitive data"""
    patterns = {
        'email': r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
        'api_key': r'api[_-]?key["\']?\s*[:=]\s*["\']([a-zA-Z0-9]{32,})["\']',
        'password': r'password["\']?\s*[:=]\s*["\']([^"\']+)["\']',
        'private_key': r'-----BEGIN (RSA|PRIVATE) KEY-----'
    }
    
    for data_type, pattern in patterns.items():
        matches = re.findall(pattern, response_text, re.IGNORECASE)
        if matches:
            self.report['findings'].append({
                'severity': 'HIGH',
                'category': 'Data Exposure',
                'issue': f'Potential {data_type} exposure detected',
                'recommendation': 'Remove sensitive data from responses'
            })

def calculate_security_score(self):
    """Calculate overall security score"""
    severity_weights = {
        'HIGH': -20,
        'MEDIUM': -10,
        'LOW': -5
    }
    
    score = 100
    for finding in self.report['findings']:
        score += severity_weights.get(finding['severity'], 0)
    
    self.report['security_score'] = max(0, score)

def generate_report(self):
    """Generate comprehensive security report"""
    self.check_https()
    self.check_ssl_certificate()
    self.check_security_headers()
    self.check_cookie_security()
    self.calculate_security_score()
    
    return self.report

def print_report(self):
    """Print formatted security report"""
    report = self.generate_report()
    
    print("=" * 80)
    print(f"SECURITY AUDIT REPORT")
    print("=" * 80)
    print(f"Target: {report['url']}")
    print(f"Scan Date: {report['scan_date']}")
    print(f"Security Score: {report['security_score']}/100")
    print("=" * 80)
    
    if not report['findings']:
        print("\n✓ No security issues found!")
    else:
        severity_order = {'HIGH': 1, 'MEDIUM': 2, 'LOW': 3}
        sorted_findings = sorted(
            report['findings'],
            key=lambda x: severity_order.get(x['severity'], 4)
        )
        
        for finding in sorted_findings:
            severity_color = {
                'HIGH': '🔴',
                'MEDIUM': '🟠',
                'LOW': '🟡'
            }
            
            print(f"\n{severity_color.get(finding['severity'], '⚪')} {finding['severity']} - {finding['category']}")
            print(f"   Issue: {finding['issue']}")
            print(f"   Recommendation: {finding['recommendation']}")
    
    print("\n" + "=" * 80)
    print("REMEDIATION SUMMARY")
    print("=" * 80)
    
    high_count = sum(1 for f in report['findings'] if f['severity'] == 'HIGH')
    medium_count = sum(1 for f in report['findings'] if f['severity'] == 'MEDIUM')
    low_count = sum(1 for f in report['findings'] if f['severity'] == 'LOW')
    
    print(f"High Priority: {high_count}")
    print(f"Medium Priority: {medium_count}")
    print(f"Low Priority: {low_count}")
    print("\nRecommended Actions:")
    print("1. Address all HIGH severity issues immediately")
    print("2. Plan remediation for MEDIUM severity issues")
    print("3. Review and fix LOW severity issues when possible")
Example usage
if name == "main":
import sys

text
if len(sys.argv) < 2:
    print("Usage: python security_audit.py <target_url>")
    print("Example: python security_audit.py https://example.com")
    sys.exit(1)

target = sys.argv[21]

print("\n⚠️  ETHICAL NOTICE:")
print("Only scan systems you own or have permission to test.")
print("Unauthorized scanning may be illegal.\n")

response = input(f"Do you have permission to scan {target}? (yes/no): ")
if response.lower() != 'yes':
    print("Scan cancelled.")
    sys.exit(0)

auditor = SecurityAuditor(target)
auditor.print_report()
```

## Technical Requirements

1. **Comprehensive security checks**
2. **Severity classification system**
3. **Detailed reporting with recommendations**
4. **Scoring mechanism**
5. **Export options** (JSON, PDF, HTML)
6. **Permission verification**

## Ethical Requirements

**MANDATORY:**
- Permission verification before scanning
- Rate limiting to avoid DoS
- Respect robots.txt
- Clear documentation of scope
- No exploitation of found vulnerabilities

## Dependencies
```
requests>=2.31.0
cryptography>=41.0.0
dnspython>=2.4.0
python-whois>=0.8.0
```


## Submission Requirements

Folder `SecurityAuditor_YourGitHubUsername` containing:

1. `security_audit.py` - Main auditor
2. `checklist.md` - Security checklist
3. `README.md` - Complete documentation
4. `requirements.txt` - Dependencies
5. `sample_reports/` - Example audit reports
6. `ETHICAL_USE.md` - Usage guidelines

## Report Requirements

Generated reports must include:
- Executive summary
- Vulnerability categorization by severity
- Detailed findings with evidence
- Remediation recommendations
- Compliance mapping (OWASP, NIST)
- Security score calculation

## Resources

- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [CIS Benchmarks](https://www.cisecurity.org/cis-benchmarks/)
- [Security Headers](https://securityheaders.com/)
- [SSL Labs](https://www.ssllabs.com/)
