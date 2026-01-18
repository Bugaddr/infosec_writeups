# Challenge 8: Blind Spot

**Category:** Miscellaneous  
**Difficulty:** Hard  
**Status:** ❌ Unsolved

## Description

Unknown - Purpose requires deeper analysis and context.

## Files

- `makeqr.py` - QR code generator with SQL injection payloads

## Analysis

### File: makeqr.py

The provided Python script generates QR codes containing SQL injection payloads:

```python
import qrcode
import random
from PIL import Image
import os
import time

# SQL injection payloads
sql_injections = [
    "' OR 1=1 -- -",
    "' OR 1=1 -- #",
    "' OR '1'='1",
    "' OR '1'='1'--",
    "'; DROP TABLE users;--",
    "'; SELECT * FROM users WHERE username='admin'--",
    "'; DELETE FROM users WHERE username='admin'--",
    "'; UPDATE users SET password='hacked' WHERE username='admin'--",
    "' UNION SELECT username, password FROM users--",
    "' UNION SELECT NULL, NULL, NULL, table_name FROM information_schema.tables--"
]

# Generate 10 QR codes
for i in range(10):
    random_injection = random.choice(sql_injections)
    data = 'roninja' + random_injection
    filename = f"qr_code_{i}.png"
    generate_qr_code(data, filename)

# Display QR codes
for i in range(10):
    filename = f"qr_code_{i}.png"
    img = Image.open(filename)
    img.show()
    time.sleep(2)
```

### Observations

1. **QR Code Generation** - Creates 10 QR codes
2. **SQL Injection Content** - Each QR encodes SQL injection + "roninja" prefix
3. **Randomization** - Different payload each time
4. **Display Loop** - Shows each QR code with 2-second delay

### Possible Challenge Scenarios

#### Scenario 1: QR Code Cracking
- Scan the QR codes to extract SQL payloads
- Identify the pattern or hidden message
- Use payloads to exploit a database

#### Scenario 2: Blind SQL Injection
- "Blind Spot" may refer to blind SQL injection
- QR codes contain payloads for extracting database data bit-by-bit
- Challenge involves exploiting without seeing results

#### Scenario 3: Social Engineering
- QR codes are used to trick users
- Scanning leads to database attack
- Challenge involves creating or analyzing such attack vectors

#### Scenario 4: Code Analysis
- Analyze the script to understand the attack pattern
- Extract flag from QR code data
- Reverse engineer the payload generation

## Key Questions

- [ ] Is this a challenge to **generate** QR codes with payloads?
- [ ] Is this a challenge to **scan** QR codes and exploit them?
- [ ] Is the flag **encoded in the payloads**?
- [ ] Is the flag **in the script itself**?
- [ ] Does the script need to be **modified** or **executed**?

## Potential Attack Vectors

| Vector | Approach |
|--------|----------|
| QR Payload Extraction | Scan/decode QR codes to get SQL injections |
| Database Exploitation | Use extracted payloads against backend DB |
| Blind SQLi | Extract data from error messages or timing |
| Union-based SQLi | `UNION SELECT` payloads for data extraction |
| Stacked Queries | `; DROP TABLE` for destructive attacks |

## Missing Context

To solve this challenge, we need:
- [ ] Challenge description/objective
- [ ] QR codes to analyze (if this generates them)
- [ ] Target database/application
- [ ] Expected flag format
- [ ] Exploitation target

## Related Skills

- QR code generation and scanning
- SQL injection techniques
- Database enumeration
- Error-based SQLi
- Blind SQLi (time-based, Boolean-based)
- Union-based SQLi

## Tools That Would Help

- **QR Scanner** - Scan and decode QR codes
- **SQL Map** - Automated SQL injection testing
- **Wireshark** - Network traffic analysis
- **Burp Suite** - Web application testing
- **Python** - Custom exploitation scripts

## Next Steps

1. **Understand the challenge objective** - What exactly needs to be done?
2. **Examine generated QR codes** - Decode and analyze payloads
3. **Identify the target** - What application/database is being attacked?
4. **Test payloads** - Try SQL injection on backend
5. **Extract flag** - Use successful payloads to get the flag

## Flag Format

`HQX{...}`

---

**Status:** This challenge remains unsolved. Additional context or the actual challenge webpage/application is needed to proceed.

**Notes:**
- The script generates SQL injection QR codes but lacks context
- Challenge objective is unclear without the actual challenge description
- Recommend examining the original challenge page or problem statement
