# Challenge 4: Press to Reveal

**Category:** Cryptography / Miscellaneous  
**Difficulty:** Medium  
**Status:** ✅ Solved

**Flag:** `HQX{66fe7ad2590ac727403ab930598747ee}`

## Description

Decode ROT47-encoded data containing JavaScript keycodes and extract the hidden flag.

## Challenge Overview

The challenge provides ROT47-encoded data that, when decoded, appears to be JavaScript keycodes. The "keycodes" are misdirection—the actual signal is a hexadecimal string hidden within.

## Solution Steps

### Step 1: Apply ROT47 Decoding

ROT47 is a simple substitution cipher. Applying it to the encoded data reveals:

```javascript
const key = [
  72, 81, 88, 219, 54, 54, 70, 188, 69, 55, 65, 189, 68, 50, 53, 57, 189,
  48, 65, 67, 34, 55, 50, 55, 52, 189, 48, 51, 27, 65, 66, 57, 17, 51,
  48, 33, 53, 57, 56, 55, 20, 52, 55, 69, 187, 69, 221
];
```

### Step 2: Identify and Remove Noise

Several values represent non-printing control keys used as noise:

| Keycode | Meaning  | ASCII |
|---------|----------|-------|
| 17      | Ctrl     | Control key |
| 20      | CapsLock | Lock key |
| 27      | Escape   | ESC |
| 33      | PageUp   | Navigation |

These do NOT contribute to the flag and must be removed.

### Step 3: Filter Out Structural Characters

Values like `219`, `221`, `187–189`, `188` are structural separators and don't encode data.

### Step 4: Identify Real Payload

After removing noise and separators, the remaining values resolve to:
- **Digits:** 0–9 (ASCII 48–57)
- **Letters:** a–f (ASCII 97–102)

This is a **hexadecimal string**!

### Step 5: Extract Hex String

Collect all hex-representing keycodes:

```
66fe7ad2590ac727403ab930598747ee
```

### Step 6: Format as Flag

Apply the required flag format `HQX{}`:

```
HQX{66fe7ad2590ac727403ab930598747ee}
```

## Decoding Tools

### Online ROT47 Decoders
- Supports rot47 from CyberChef
- Quick-and-dirty: `rot47` from online cipher tools

### Manual Analysis
```python
def rot47_decode(s):
    result = []
    for c in s:
        if 33 <= ord(c) <= 126:
            result.append(chr(33 + (ord(c) - 33 - 47) % 94))
        else:
            result.append(c)
    return ''.join(result)
```

## Key Insights

1. **ROT47 can hide structured data** within apparent chaos
2. **Control keycodes serve as effective noise injection** to obscure the signal
3. **"JavaScript keycode" is misdirection** - the real hint is hex character codes
4. **Systematic filtering reveals patterns** - remove noise, identify structure
5. **Hex strings are common flag formats** - especially after decryption

## Attack Checklist

- [ ] Identify the encoding (ROT47)
- [ ] Decode the ciphertext
- [ ] Classify values (control keys, data, separators)
- [ ] Remove noise (control keys, structural values)
- [ ] Identify the remaining pattern (hex digits)
- [ ] Extract and format the flag

## Lessons Learned

- Cryptographic misdirection is a powerful CTF technique
- Multiple encoding layers require systematic analysis
- Understanding ASCII codes is essential
- Hex is a common format for encoded data
- Always question narrative hints in challenges

## Flag Format

```
HQX{66fe7ad2590ac727403ab930598747ee}
```
