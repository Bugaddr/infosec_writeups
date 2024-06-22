#  She Is My "X"
150

Now i have to brute force and decrypt also ?

https://drive.google.com/file/d/1fTm2PahIb0NGbcGpDDo9oKDU-SEXuIzV/view?usp=sharing

Flag Format: THMCTF{a-zA-Z0-9}

Author: cursed_hacker

## Solution

1. The original code below encrypts the flag by xoring each character with random value a (1 to 500) and then shifts that xor'ed value with a random (1-100) places hence giving final encrypted ascii array 
```python
   from random import randint

flag = "THMCTF{h3h3_1_l0v3_7hm}"
a = randint(1, 500)
shift = randint(1, 100)
encrypted_flag = []

for char in flag:
    x_encrypted_value = ord(char) ^ a
    scissor_encrypted_value = (x_encrypted_value + shift) % 256
    encrypted_flag.append(str(scissor_encrypted_value))

print(encrypted_flag)

#encrypted_flag = ['134', '162', '159', '153', '134', '148', '177', '230', '190', '190', '141', '229', '194', '233', '141', '233', '188', '185', '168', '179', '170', '229', '235', '234', '188', '141', '180', '234', '168', '141', '229', '194', '235', '231', '141', '231', '229', '167', '170', '235', '182', '141', '180', '190', '230', '228', '175']
```

2. To decrypt it, we can use the below script that will try all permutations and combinations of shift along with xored a value hence generating 100x500 various combinations of output for encrypted_flag
```python
encrypted_flag = ['134', '162', '159', '153', '134', '148', '177', '230', '190', '190', '141', '229', '194', '233', '141', '233', '188', '185', '168', '179', '170', '229', '235', '234', '188', '141', '180', '234', '168', '141', '229', '194', '235', '231', '141', '231', '229', '167', '170', '235', '182', '141', '180', '190', '230', '228', '175']

# Iterate through all possible values of a and shift
for a in range(1, 501):
    for shift in range(1, 101):
        decrypted_flag = []
        try:
            # Step 1: Convert encrypted values to integers
            encrypted_integers = [int(value) for value in encrypted_flag]

            # Step 2: Reverse the shift operation
            x_encrypted_values = [(value - shift) % 256 for value in encrypted_integers]

            # Step 3: Reverse the XOR operation
            decrypted_ascii_values = [x ^ a for x in x_encrypted_values]

            # Step 4: Convert ASCII values to characters
            decrypted_characters = ''.join(chr(value) for value in decrypted_ascii_values)

            # Print potential flag if it contains only printable ASCII characters
            if all(chr(value).isprintable() for value in decrypted_ascii_values):
                print(f"Decrypted flag with a={a}, shift={shift}: {decrypted_characters}")

        except Exception as e:
            continue
```

3. After executing the above script with `python3 script.py >> generated_output.txt` we can grep the flag with `grep THMCTF generated_output.txt` to get the flag
