# Challenge 5: Whitespace Warrior

**Category:** Steganography  
**Difficulty:** Hard  
**Status:** ✅ Solved

**Flag:** `HQX{ece2d9946ca8707adafd31dae37358bb}`

## Description

Decode binary data hidden in zero-width Unicode characters embedded within normal text.

## Challenge Overview

A normal-looking English paragraph contains a hidden flag encoded using invisible zero-width Unicode characters. The challenge is to extract and decode these characters to reveal the flag.

## Files

- `F6fA8af2de.txt` - Steganographic text with embedded zero-width characters
- `decoder.py` - Python script to extract and decode hidden data
- `finalsolver.py` - Alternative decoding approach
- `soluton.md` - Detailed writeup

## Solution

### Steganography Technique

The flag is encoded using two zero-width Unicode characters:

| Character | Unicode | Name | Purpose |
|-----------|---------|------|---------|
| ZWSP | U+200B | Zero Width Space | Binary carrier (0 or 1) |
| ZWNJ | U+200C | Zero Width Non-Joiner | Binary carrier (0 or 1) |

These characters are **invisible** to the human eye but present in the UTF-8 encoded text.

### Encoding Logic

1. **Flag → ASCII** - Convert each character to 8-bit ASCII
2. **ASCII → Binary** - Each byte becomes 8 bits
3. **Binary → Unicode** - Map bits to zero-width characters:
   - Either: `0 → ZWSP, 1 → ZWNJ`
   - Or: `0 → ZWNJ, 1 → ZWSP` (randomized)
4. **Hide in text** - Inject encoded bits into normal paragraph

### Decoding Script

```python
ZWSP = "\u200b"   # Zero Width Space
ZWNJ = "\u200c"   # Zero Width Non-Joiner

with open("F6fA8af2de.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Step 1: Extract only zero-width characters
hidden = [c for c in text if c in (ZWSP, ZWNJ)]

def decode(zero, one):
    """Attempt decoding with given bit mappings"""
    bits = ''.join('0' if c == zero else '1' for c in hidden)
    
    # Try all 8 possible bit offsets
    for offset in range(8):
        out = ""
        chunk = bits[offset:]
        
        # Convert each 8-bit chunk to ASCII character
        for i in range(0, len(chunk), 8):
            byte = chunk[i:i+8]
            if len(byte) == 8:
                out += chr(int(byte, 2))
        
        # Valid flags contain '{'
        if "{" in out:
            return out

# Try both possible bit mappings
flag = decode(ZWNJ, ZWSP) or decode(ZWSP, ZWNJ)
print(flag)
```

### Decoding Steps

1. **Read file** with UTF-8 encoding
2. **Extract zero-width characters** - filter for ZWSP and ZWNJ only
3. **Map to bits** - Convert characters to binary string
4. **Brute-force bit offsets** - Try all 8 possible alignments
5. **Convert to ASCII** - Every 8 bits becomes one character
6. **Find valid output** - Flag contains `{}`

## Key Challenges

- **Binary misalignment** - Correct bit offset must be found via brute-force
- **Randomized encoding** - Bit mapping varies (0→ZWSP or 0→ZWNJ)
- **Invisible characters** - Visual inspection reveals nothing
- **Unicode awareness** - Must use proper UTF-8 encoding

## Detection Methods

### Manual Detection
1. Copy text from challenge
2. Paste into Unicode inspector (e.g., Chardet, Unicode analyzer)
3. Look for character codes U+200B, U+200C between visible text

### Python Detection
```python
with open("F6fA8af2de.txt", "r", encoding="utf-8") as f:
    text = f.read()

zwsp_count = text.count("\u200b")
zwnj_count = text.count("\u200c")

print(f"ZWSP occurrences: {zwsp_count}")
print(f"ZWNJ occurrences: {zwnj_count}")
```

## Related Techniques

- **Zero-width joiner (ZWJ)** - Used in Emoji sequences
- **Soft hyphens** - U+00AD for line breaking
- **Unicode homoglyphs** - Similar-looking characters
- **Homograph attacks** - Domain spoofing with Unicode
- **Combining characters** - Stacking diacritics

## Lessons Learned

1. **Invisible doesn't mean gone** - Zero-width characters are still in the data
2. **Unicode is complex** - Many characters exist for specific purposes
3. **Binary encoding is powerful** - Any 2-character set can encode binary
4. **Brute-forcing is necessary** - Randomization requires trying all options
5. **Steganography vs. Cryptography** - This is hiding, not encrypting

## Tools Used

- **Python** - Text processing and binary conversion
- **Text editor** - Unicode detection (VS Code, Sublime)
- **Chardet** - Character encoding detection
- **Wireshark** - Network traffic inspection (if needed)

## Attack Checklist

- [ ] Identify the steganography type (zero-width characters)
- [ ] Extract suspicious Unicode characters
- [ ] Map to binary representation
- [ ] Try both bit mappings (0→ZWSP vs 0→ZWNJ)
- [ ] Brute-force all 8 bit offsets
- [ ] Convert binary chunks to ASCII
- [ ] Detect valid output (contains `{`)
- [ ] Extract and format flag

## Flag Format

```
HQX{ece2d9946ca8707adafd31dae37358bb}
```
