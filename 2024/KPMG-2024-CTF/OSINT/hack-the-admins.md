# Hacking the admins

Raghava Sai Sarvan really loves cat

## Approach

1. Simple google search with term `Raghava Sai Sarvan` comes up with Linkedin account of `https://www.linkedin.com/in/raghavasaissh/?originalSu` whose about states:

    ```text
    Decode ;) TmV2ZXIgZ29ubmEgZ2l2ZSB5b3UgdXAKTmV2ZXIgZ29ubmEgbGV0IHlvdSBkb3duCk5ldmVyIGdvbm5hIHJ1biBhcm91bmQgYW5kIGRlc2VydCB5b3UKTmV2ZXIgZ29ubmEgbWFrZSB5b3UgY3J5Ck5ldmVyIGdvbm5hIHNheSBnb29kYnllCk5ldmVyIGdvbm5hIHRlbGwgYSBsaWUgYW5kIGh1cnQgeW91CgpodHRwczovL3Bhc3RlYmluLmNvbS9uWm1ibkJRMyAtIG1lb3c=
    ```

2. This can be decoded using base64, which gives:

    ```text
    Never gonna give you up
    Never gonna let you down
    Never gonna run around and desert you
    Never gonna make you cry
    Never gonna say goodbye
    Never gonna tell a lie and hurt you

    https://pastebin.com/nZmbnBQ3 - meow
    ```

3. Opening <https://pastebin.com/nZmbnBQ3> with meow gives

    ```text
    https://www.linkedin.com/in/saurabh-bhatt-cybersecurity/
    
    check out my discord - eren_meow if you like cats, check it if you don't also
    ```

4. Saurabh bhatt's profile has about section with string `5k2tWE6P7gjtw4iCUSTTeNFaxbTu4WVfoGHgfE73` which can be decoded with base58 which gives <https://pastebin.com/KM65Tw0R> and password for this is in description of eren_meow discord account `44WkWTAaTZM1pKThjQk2c - this is a username or a password` which is again base58 encoded, and gives `meowsaurabh123!` as password.
5. That again came up with:

    ```text
    https://www.linkedin.com/in/aditya-kashinath-4042a1186/
    
    
    ++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>>+++++++.--.+++++++++++..+++++.<<++++++++++++++++.>>----------.---..+++++++++++++.<<.>>----------------------.+++++.-------.+++++++++++++.
    ```

    this is brainfuck, which after running gives out `kitty.olly.chan` that can be used as password on `https://pastebin.com/KVn2Y9uk` and this gives

    ```text
    Oh no you caught me, here you go:

    KPMG_CTF{71f920fa275127a7b60fa4d4d41432a3}
    ```
