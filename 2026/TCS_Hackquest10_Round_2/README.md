# TCS HackQuest Round 2 - CTF WriteUps (Ai generated writeups for my origianl files)

A collection of solutions for TCS HackQuest Round 2 challenges. These writeups document the methodology, tools, and key insights for solving each challenge.

---

## Challenge Index

| # | Name | Category | Difficulty | Status |
|---|------|----------|------------|--------|
| 1 | [Misfit](#1-misfit) | Steganography | Easy | ✅ Solved |
| 2 | [Timelock](#2-timelock) | Web / Misc | Easy | ✅ Solved |
| 3 | [Quietlock](#3-quietlock) | Network / Forensics | Medium | ✅ Solved |
| 4 | [Press to Reveal](#4-press-to-reveal) | Cryptography / Misc | Medium | ✅ Solved |
| 5 | [Whitespace Warrior](#5-whitespace-warrior) | Steganography | Hard | ✅ Solved |
| 6 | [Vanishing Point](#6-vanishing-point) | Web | Medium | ✅ Solved |
| 7 | [Pursuit of Secrets](#7-pursuit-of-secrets) | Web / Exploitation | Hard | 🔄 Partial |
| 8 | [Blind Spot](#8-blind-spot) | Miscellaneous | Hard | ❌ Unsolved |

---

## Solved Challenges

### 1. Misfit

**Category:** Steganography | **Difficulty:** Easy

**Description:** Extract hidden messages from mixed-case text using character filtering.

**Solution:**
- Extract uppercase letters: `grep -o '[A-Z]' text2 | tr -d '\n'`
- Extract lowercase letters: `grep -o '[a-z]' text2 | tr -d '\n'`
- Combine results to form the flag

**Key Commands:**
```bash
grep -o '[A-Z]' text2 | tr -d '\n'   # Uppercase only
grep -o '[a-z]' text2 | tr -d '\n'   # Lowercase only
```

**Takeaway:** Simple filtering can reveal hidden patterns in plaintext steganography.

---

### 2. Timelock

**Category:** Web / Misc | **Difficulty:** Easy

**Description:** Bypass a web timer that requires hours of elapsed time.

**Solution:**
The webpage tracks elapsed time in browser localStorage. Instead of waiting hours, directly manipulate the localStorage value to simulate the required elapsed time:

```javascript
localStorage.setItem(
  "timelock_v1_data",
  JSON.stringify({
    elapsed: 12.5 * 60 * 60 * 1000  // 12.5 hours in milliseconds
  })
);
location.reload();
```

**Approach:**
1. Open browser DevTools (F12)
2. Go to Console tab
3. Paste the code above
4. Page will reload with simulated elapsed time
5. Flag is revealed

**Takeaway:** Client-side validation is insecure; timing mechanisms can be trivially bypassed.

---

### 3. Quietlock

**Category:** Network / Forensics | **Difficulty:** Medium

**Description:** Analyze packet capture to find hidden communications.

**Solution:**
Use Wireshark to filter DNS-over-HTTPS traffic. The key is identifying POST requests to specific DNS providers:

**Wireshark Filter:**
```
http.request.method == "POST" && http.host == "dns.google"
```

**Approach:**
1. Open the PCAP file in Wireshark
2. Apply the filter above
3. Extract POST data from DNS queries
4. Decode the DNS-over-HTTPS payload

**Takeaway:** DNS traffic can hide command-and-control communications; proper filtering reveals anomalies.

---

### 4. Press to Reveal

**Category:** Cryptography / Misc | **Difficulty:** Medium

**Flag:** `HQX{66fe7ad2590ac727403ab930598747ee}`

**Description:** Decode ROT47-encoded data containing JavaScript keycodes.

**Solution Steps:**

1. **Apply ROT47 decoding** to extract a JavaScript keycode array:
   ```js
   const key = [
     72, 81, 88, 219, 54, 54, 70, 188, 69, 55, 65, 189, 68, 50, 53, 57, 189,
     48, 65, 67, 34, 55, 50, 55, 52, 189, 48, 51, 27, 65, 66, 57, 17, 51,
     48, 33, 53, 57, 56, 55, 20, 52, 55, 69, 187, 69, 221
   ];
   ```

2. **Remove noise (control keycodes):**
   - `17` = Ctrl
   - `20` = CapsLock
   - `27` = Escape
   - `33` = PageUp

3. **Identify meaningful values:** Remaining codes represent hex characters (0-9, a-f)

4. **Reconstruct hex string:**
   ```
   66fe7ad2590ac727403ab930598747ee
   ```

5. **Format as flag:**
   ```
   HQX{66fe7ad2590ac727403ab930598747ee}
   ```

**Key Insights:**
- ROT47 can hide structured data within apparent chaos
- Control keycodes serve as effective noise injection
- Misdirection via "JavaScript keycode" hints requires careful analysis

---

### 5. Whitespace Warrior

**Category:** Steganography | **Difficulty:** Hard

**Flag:** `HQX{ece2d9946ca8707adafd31dae37358bb}`

**Description:** Decode binary data hidden in zero-width Unicode characters.

**Solution:**

The hidden flag is encoded using zero-width Unicode characters embedded in normal text:
- **ZWSP** (Zero Width Space) = `U+200B`
- **ZWNJ** (Zero Width Non-Joiner) = `U+200C`

**Decoding Script:**
```python
ZWSP = "\u200b"   # Zero Width Space
ZWNJ = "\u200c"   # Zero Width Non-Joiner

with open("F6fA8af2de.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Extract only zero-width characters
hidden = [c for c in text if c in (ZWSP, ZWNJ)]

def decode(zero, one):
    """Try decoding with given bit mappings"""
    bits = ''.join('0' if c == zero else '1' for c in hidden)
    for offset in range(8):
        out = ""
        chunk = bits[offset:]
        for i in range(0, len(chunk), 8):
            byte = chunk[i:i+8]
            if len(byte) == 8:
                out += chr(int(byte, 2))
        if "{" in out:
            return out

# Try both possible mappings
flag = decode(ZWNJ, ZWSP) or decode(ZWSP, ZWNJ)
print(flag)
```

**Key Insights:**
- Invisible Unicode characters are effective for steganography
- Always inspect suspicious text at the Unicode level
- Randomized encodings require systematic brute-forcing
- Bit misalignment is common in text-based stego challenges

---

### 6. Vanishing Point

**Category:** Web | **Difficulty:** Medium

**Flag:** `HQX{c51e54704c0cad1e5c2029a576588f58}`

**Description:** Extract and reuse session-specific credentials before auto-refresh.

**Challenge Analysis:**

The webpage auto-reloads every 5 seconds via client-side JavaScript:
```js
setInterval(() => {
    location.reload();
}, 5000);
```

Credentials are exposed in HTML comments and regenerated per session:
```html
<!-- Username="hquser-<random>" -->
<!-- Password="<random>" -->
```

**Vulnerability:** Client-side enforcement allows JavaScript-independent clients (like `curl`) to preserve the initial session.

**Exploitation:**

```bash
# Step 1: Fetch page and capture session cookie
curl -s -c cookies.txt http://challenge.tcshackquest.com:12960/

# Step 2: Extract credentials from HTML comments
curl -s -c cookies.txt http://challenge.tcshackquest.com:12960/ \
  | grep -oP 'Username="\K[^"]+|Password="\K[^"]+'

# Step 3: Login with extracted credentials (same session)
curl -b cookies.txt -X POST http://challenge.tcshackquest.com:12960/ \
  -d "username=hquser-<extracted>&password=<extracted>"
```

**Root Causes:**
- Sensitive information disclosure (credentials in HTML comments)
- Client-side security dependency
- Session-bound credentials without server-side validation
- TOCTOU (Time-of-Check Time-of-Use) logic flaw

**Key Lessons:**
- Never rely on JavaScript for security
- HTML comments are visible in raw requests
- Tools like `curl` bypass client-side protections entirely

---

## Partial / Unsolved Challenges

### 7. Pursuit of Secrets

**Category:** Web / Exploitation | **Difficulty:** Hard | **Status:** 🔄 Partial

**Description:** A cat bypassed image checks using an alternative data stream trick to access restricted files.

**Hints:**
- Image validation can be bypassed
- Alternative data streams (e.g., ADS on NTFS, alternate file streams)
- Chat about the method is in `/mail/secret.eml`

**Notes:** Requires further investigation into NTFS alternate data streams or similar file system tricks.

---

### 8. Blind Spot

**Category:** Miscellaneous | **Difficulty:** Hard | **Status:** ❌ Unsolved

**Description:** Unknown - requires deeper analysis.

**Files Present:**
- `makeqr.py` - Generates QR codes with SQL injection payloads

**Notes:** Appears to involve QR code generation and SQL injection testing. Purpose unclear without additional context.

---

## Tools Used

- **grep** - Text filtering and pattern matching
- **curl** - HTTP requests and session management
- **Wireshark** - Network packet analysis
- **Python** - Custom decoding scripts
- **Browser DevTools** - Client-side manipulation
- **ROT47 decoder** - Cipher reversal
- **Unicode inspector** - Character-level analysis

---

## Security Lessons Learned

1. **Client-side security is no security** - Always validate server-side
2. **Steganography can hide anywhere** - Text, images, DNS traffic, Unicode characters
3. **Comments are not private** - HTML comments appear in raw requests
4. **Data streams matter** - File system features can bypass validation
5. **Timing attacks work** - Time-based checks are bypassed via client manipulation
6. **Misdirection is powerful** - CTF challenges often include intentional false leads

---

## Repository Structure

```
hackquest.bak/
├── README.md                          # This file
├── 1misfit/
│   ├── solution                       # Command history
│   ├── text                           # Steganography source
│   └── text2                          # Steganography source
├── 2timelock/
│   └── run_in_console                 # Exploit code
├── 3quietlock/
│   ├── 42beBe5691.pcap               # Network capture
│   ├── wireshark_filter              # Filter syntax
│   └── aianswer                      # Analysis notes
├── 4presstoreveal/
│   ├── Aab1a889a6file.enc            # Encoded data
│   └── solution.txt                  # Writeup
├── 5whitespace_warrior/
│   ├── F6fA8af2de.txt               # Steganographic text
│   ├── decoder.py                    # Decoding script
│   ├── finalsolver.py                # Alternative solver
│   └── soluton.md                    # Writeup
├── 6vanishingpoint/
│   ├── c.txt                         # Exploit cookies
│   ├── site.html                     # Challenge source
│   └── solution.md                   # Writeup
├── 7pursuits_of_secrets/
│   ├── description.md                # Challenge description
│   ├── download_image                # Challenge binary
│   └── webpage.html                  # Challenge interface
└── 8blind_spot/
    └── makeqr.py                     # QR code generator
```

---

## Summary

**Solved:** 6/8 challenges  
**Partial:** 1/8 challenges  
**Unsolved:** 1/8 challenges  

This writeup collection demonstrates a wide range of attack vectors including steganography, web exploitation, cryptanalysis, network forensics, and client-side bypass techniques. Each challenge reinforces the importance of thorough enumeration, creative thinking, and understanding both offensive and defensive security principles.

---

*Last updated: January 2026*
