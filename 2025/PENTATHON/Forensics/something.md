# Code

```python
import struct
import zlib
 
# Mapping from the lowercase (or mis-ordered) version to the correct chunk name.
CHUNK_MAPPING = {
    b"ihdr": b"IHDR",
    b"plte": b"PLTE",
    b"idat": b"IDAT",  # if correctly spelled as "idat"
    b"iadt": b"IDAT",  # fix misordering: iadt -> IDAT
    b"iend": b"IEND",
    b"phys": b"pHYs",  # physical pixel dimensions must be exactly "pHYs"
    b"text": b"tEXt",
    b"itxt": b"iTXt",
    b"ztxt": b"zTXt"
}
 
def fix_chunk_type(orig_type):
    # Convert orig_type to bytes if needed, then lowercase it for lookup.
    key = bytes(orig_type).lower()
    if key in CHUNK_MAPPING:
        return CHUNK_MAPPING[key]
    return orig_type
 
def fix_png(filename_in, filename_out):
    with open(filename_in, "rb") as f:
        data = bytearray(f.read())
 
    # 1. Fix PNG signature: it must be 89 50 4E 47 0D 0A 1A 0A
    correct_signature = b'\x89PNG\r\n\x1a\n'
    data[0:8] = correct_signature
 
    ptr = 8  # start right after the signature
    while ptr + 8 <= len(data):
        # Read the chunk length (4 bytes, big-endian)
        chunk_length = struct.unpack(">I", data[ptr:ptr+4])[0]
        # Read the chunk type (4 bytes)
        orig_chunk_type = data[ptr+4:ptr+8]
        fixed_chunk_type = fix_chunk_type(orig_chunk_type)
        if orig_chunk_type != fixed_chunk_type:
            try:
                old_name = orig_chunk_type.decode("ascii")
            except UnicodeDecodeError:
                old_name = str(orig_chunk_type)
            new_name = fixed_chunk_type.decode("ascii")
            print(f"Fixing chunk type '{old_name}' to '{new_name}' at offset {ptr+4}")
            data[ptr+4:ptr+8] = fixed_chunk_type
 
        # Calculate new CRC for the chunk (over chunk type and chunk data)
        chunk_data = data[ptr+8:ptr+8+chunk_length]
        crc_input = data[ptr+4:ptr+8+chunk_length]  # chunk type + data
        new_crc = zlib.crc32(crc_input) & 0xffffffff
        # Write new CRC (4 bytes, big-endian)
        crc_offset = ptr + 8 + chunk_length
        data[crc_offset:crc_offset+4] = struct.pack(">I", new_crc)
 
        # Move pointer to next chunk: length (4) + type (4) + data (chunk_length) + CRC (4)
        ptr += 8 + chunk_length + 4
 
    with open(filename_out, "wb") as f:
        f.write(data)
    print(f"Fixed PNG saved as '{filename_out}'.")
 
# Example usage:
fix_png("weird.png", "fixed.png")
```
