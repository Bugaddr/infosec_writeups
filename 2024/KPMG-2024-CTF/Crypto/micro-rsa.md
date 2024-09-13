# Micro RSA - 100

1. Function to find the integer cube root

    ```
    def integer_cube_root(n):
    low = 0
    high = n
    while low < high:
    mid = (low + high) // 2
    if mid**3 < n:
    low = mid + 1
    else:
    high = mid
    return low
    ```

2. Provided RSA components

    ```
    n = 124654455290240170438072831687154216330318678151127912274279675542477378324205547190448356708255017687037267403854771170485302392671467974951403923256433631043504787586559727625072674672756729381597771352105733117303538360769540765664178969569213281846028712352533347099724394655235654023223677262377960566427
    e = 3
    c = 11127001790949419009337112638492797447460274274218482444358708583659626034144288836997001734324915439994099506833199252902923750945134774986248955381033641128827831707738209340996252344658078512599270181951581644119582075332702905417250405953125
    ```

3. Find the cube root of c

    ```
    m = integer_cube_root(c)
    ```

4. Verify if it's the correct cube root

    ```
    if m**3 == c:
    decoded_message_number = m
    try:
    decoded_message_text = bytearray.fromhex(hex[decoded_message_number](2:)).decode()
    except Exception as e:
    decoded_message_text = f"Could not decode as text: {e}"
    else:
    decoded_message_number = None
    decoded_message_text = "No exact cube root found. Further factorization or methods may be required."

    (decoded_message_number, decoded_message_text)
    ```

flag is KPMG_CTF{sm4ll_e_15_n07_s0_s3cur3}
