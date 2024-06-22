#  Damaged
100

Oh no my file has been corrupted can you help me fix it.

https://drive.google.com/file/d/1fHl4O28axCfTkNn5sT80KYbf4fp16XC-/view?usp=sharing

Flag Format: ThunderCipher{a-zA-Z0-9}

Author: 0x1337

# SOlution

1. Unzip the zip it has file named damaged which has IHDR visible in hexeditor so it is png but header is corrupted
![header is fucked](assets/damaged/image.png)

2. Restore the header signature
replace `bb aa dd cc` at 0x0 to 0x3 with `89 50 4E 47`

![fixed](assets/damaged/image-2.png)

3. ![flag](assets/damaged/image-1.png)