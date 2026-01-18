Below is the **final, polished, submission-ready write-up** for **WhiteSpace Warfare – 500**, matching the **final clean script** and the **correct flag**.
You can paste this directly into a CTF platform or a GitHub writeups repo.

---

# 🧩 WhiteSpace Warfare – 500

**Category:** Steganography
**Difficulty:** Hard

---

## 🔍 Challenge Overview

The challenge provides a normal-looking English paragraph along with a blurred Python script in the background. The description hints that secrets are hidden using **“silence”**, implying that the flag is concealed using **invisible characters** rather than traditional cryptography.

---

## 🧠 Key Observation

Copying the text into a Unicode-aware editor or inspecting character codes reveals the presence of **zero-width Unicode characters** embedded between visible letters. These characters are not rendered visually but remain intact in UTF-8 encoded text.

The two characters used are:

* **Zero Width Space (ZWSP)** – `U+200B`
* **Zero Width Non-Joiner (ZWNJ)** – `U+200C`

These characters act as binary carriers.

---

## 🔬 Encoding Logic (Recovered)

From the background script logic:

1. The flag is converted into **8-bit ASCII binary**
2. Each bit is mapped to a zero-width character:

   * Either `0 → ZWSP, 1 → ZWNJ`
   * Or `0 → ZWNJ, 1 → ZWSP` (randomized)
3. The encoded data is injected into a normal paragraph
4. Bit alignment is not guaranteed, requiring brute-force offset correction

---

## 🛠️ Decoding Approach

To recover the flag:

1. Read the stego text using UTF-8 encoding
2. Extract only zero-width characters
3. Try both bit mappings
4. Brute-force all 8 possible bit offsets
5. Detect valid ASCII output containing `{`

---

## 🧪 Final Decoder Script

```python
ZWSP = "\u200b"   # Zero Width Space
ZWNJ = "\u200c"   # Zero Width Non-Joiner

with open("F6fA8af2de.txt", "r", encoding="utf-8") as f:
    text = f.read()

hidden = [c for c in text if c in (ZWSP, ZWNJ)]

def decode(zero, one):
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

flag = decode(ZWNJ, ZWSP) or decode(ZWSP, ZWNJ)
print(flag)
```

---

## 📤 Output

```
HQX{ece2d9946ca8707adafd31dae37358bb}
```

---

## 🏁 Final Flag

```
HQX{ece2d9946ca8707adafd31dae37358bb}
```

---

## 🧠 Lessons Learned

* Invisible Unicode characters are powerful steganographic tools
* Always inspect suspicious text at the **Unicode level**
* Randomized encodings require systematic brute-forcing
* Bit misalignment is common in text-based stego challenges

---

## ✅ Conclusion

This challenge demonstrates an effective use of zero-width Unicode characters to hide binary data inside plain text. By carefully extracting and decoding these characters while correcting bit alignment, the hidden flag can be reliably recovered.

---
