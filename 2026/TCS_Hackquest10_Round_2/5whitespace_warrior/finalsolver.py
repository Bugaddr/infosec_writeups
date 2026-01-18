# WhiteSpace Warfare - Final Decoder

ZWSP = "\u200b"   # Zero Width Space
ZWNJ = "\u200c"   # Zero Width Non-Joiner

# Read stego text
with open("F6fA8af2de.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Extract only zero-width characters
hidden = [c for c in text if c in (ZWSP, ZWNJ)]

def decode(zero, one):
    bits = ''.join('0' if c == zero else '1' for c in hidden)

    for offset in range(8):  # brute-force bit alignment
        out = ""
        sliced = bits[offset:]
        for i in range(0, len(sliced), 8):
            byte = sliced[i:i+8]
            if len(byte) == 8:
                out += chr(int(byte, 2))
        if "{" in out:
            return out

# Try both mappings
flag = decode(ZWNJ, ZWSP) or decode(ZWSP, ZWNJ)

print(flag)
