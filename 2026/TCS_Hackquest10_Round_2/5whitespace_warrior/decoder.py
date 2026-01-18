text = open("F6fA8af2de.txt", "r", encoding="utf-8").read()

ZWSP = "\u200b"
ZWNJ = "\u200c"

hidden = [c for c in text if c == ZWSP or c == ZWNJ]

def try_decode(zero, one):
    bits = ''.join('0' if c == zero else '1' for c in hidden)

    results = []
    for offset in range(8):   # brute bit alignment
        out = ""
        chunk = bits[offset:]
        for i in range(0, len(chunk), 8):
            byte = chunk[i:i+8]
            if len(byte) == 8:
                try:
                    out += chr(int(byte, 2))
                except:
                    pass
        results.append((offset, out))
    return results

print("=== Mapping 1 ===")
for o, r in try_decode(ZWSP, ZWNJ):
    if "{" in r:
        print("offset", o, "=>", r)

print("\n=== Mapping 2 ===")
for o, r in try_decode(ZWNJ, ZWSP):
    if "{" in r:
        print("offset", o, "=>", r)
