# Gear

150 pts

Reversing the control of Car can get you to the right Destination

<https://drive.google.com/file/d/1PH5-0s83BnVP0TD26ISg5_TU0hPSti8Y/view?usp=sharing>

Flag Format: THMNAG{a-zA-Z0-9}

Author: Parth Thakre

## Solution

1. So basically the java code does is that it takes the input and then encrypts that in following sequence:

    ```txt
    1. Input flag: ll
    2. After first Base64: bGw=
    3. After reversing: =wGb
    4. After second Base64: PXdHYg==
    5. After shifting: OWcGXf==
    6. After hex conversion: 4f57634758663d3d
    7. After XOR: 465e6a4e516f3434
    8. FInal encrypted output: 465e6a4e516f3434

    ```

2. So i have reimplemented the same code in python

    ```python
    import base64

    def reverseXor(hexInput, key, dummy):
        reversedHex = []
        for i in range(0, len(hexInput), 2):
            hexChar = int(hexInput[i:i+2], 16)
            hexChar ^= key
            reversedHex.append(format(hexChar, '02x'))
        return ''.join(reversedHex)

    def hexToString(hexInput, dummy):
        result = []
        for i in range(0, len(hexInput), 2):
            hexChar = chr(int(hexInput[i:i+2], 16))
            result.append(hexChar)
        return ''.join(result)

    def reverseShift(input, amount, dummy):
        result = []
        for c in input:
            if c.isalpha():
                base = ord('A') if c.isupper() else ord('a')
                offset = (ord(c) - base - amount) % 26
                c = chr(base + offset)
            result.append(c)
        return ''.join(result)

    def fromBase64(input, dummy):
        return base64.b64decode(input).decode()

    def reverseStr(input, dummy):
        return input[::-1]

    def reverseEncryption(hexString):
        decryptedInput = hexString
        
        # Reverse XOR with key=9
        decryptedInput = reverseXor(decryptedInput, 9, 56789)
        print("After XOR: " + decryptedInput)
        
        # Convert hex to string
        decryptedInput = hexToString(decryptedInput, 98765)
        print("After hex to string: " + decryptedInput)
        
        # Reverse shifting by amount=25
        decryptedInput = reverseShift(decryptedInput, 25, 67890)
        print("After shifting: " + decryptedInput)
        
        # Decode from Base64 with dummy=12345
        decryptedInput = fromBase64(decryptedInput, 12345)
        print("After second Base64 decode: " + decryptedInput)
        
        # Reverse string reversal
        decryptedInput = reverseStr(decryptedInput, 54321)
        print("After reversing: " + decryptedInput)
        
        # Decode from Base64 with dummy=345345345
        decryptedInput = fromBase64(decryptedInput, 345345345)
        print("Original Flag: " + decryptedInput)

    if __name__ == "__main__":
        encryptedFlag = "465a385850605c475f4c623f474a4c606d4a6f7e5f645c4f6d65443c5a6566636d636370505c4c6373385847734d5c5f"
        reverseEncryption(encryptedFlag)
    ```
