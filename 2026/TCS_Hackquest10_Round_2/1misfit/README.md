# Challenge 1: Misfit

**Category:** Steganography  
**Difficulty:** Easy  
**Status:** ✅ Solved

## Description

Extract hidden messages from mixed-case text files using character filtering techniques.

## Files

- `text` - First steganographic source file
- `text2` - Second steganographic source file  
- `solution` - Command history showing the solution approach

## Solution

The hidden message is encoded by mixing visible text with uppercase and lowercase letters that form the actual flag.

### Approach

Extract uppercase characters only:
```bash
grep -o '[A-Z]' text2 | tr -d '\n'
```

Extract lowercase characters only:
```bash
grep -o '[a-z]' text2 | tr -d '\n'
```

Combine both extractions to reconstruct the complete flag.

## Key Commands

```bash
# Extract uppercase letters and remove newlines
grep -o '[A-Z]' text2 | tr -d '\n'

# Extract lowercase letters and remove newlines
grep -o '[a-z]' text2 | tr -d '\n'
```

## Lessons Learned

- Simple character filtering can reveal hidden patterns in plaintext
- Mixed-case steganography relies on visual obscuration
- Unix tools like `grep` and `tr` are powerful for text extraction
- Always try basic filtering techniques before complex analysis

## Flag Format

`HQX{...}`
