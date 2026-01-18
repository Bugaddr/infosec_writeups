# Challenge 7: Pursuit of Secrets

**Category:** Web / File System Exploitation  
**Difficulty:** Hard  
**Status:** 🔄 Partial / Incomplete

## Description

A sneaky cat bypassed image file validation checks using an alternative data stream trick to access restricted files.

## Challenge Overview

The challenge involves:
- Image upload/validation mechanisms
- File system tricks to bypass checks
- Access to restricted files (e.g., `/mail/secret.eml`)
- Alternative file streams or similar techniques

## Files

- `description.md` - Challenge description
- `webpage.html` - Challenge interface
- `download_image` - Challenge binary/tool

## Key Clues

From the description:
> "A sneaky cat slipped past our image checks using a clever trick and peeked into files in odd ways."

This suggests:
1. **Image validation bypass** - The file appears to be an image but isn't
2. **Alternative file streams** - NTFS Alternate Data Streams (ADS) or similar
3. **File access trick** - Viewing files through alternate I/O streams
4. **Email involvement** - Secret information in `/mail/secret.eml`

## Potential Attack Vectors

### 1. NTFS Alternate Data Streams (ADS)

On Windows NTFS, files can have multiple data streams:

```bash
# Create file with hidden stream
echo "hidden" > file.txt:secret.txt

# Access hidden stream
type file.txt:secret.txt

# List all streams
dir /R file.txt
```

A file like `image.jpg:shell.exe` would appear as an image but execute code.

### 2. Polyglot Files

Files that are valid in multiple formats:
- Valid PNG AND valid ZIP
- Valid JPEG AND valid PDF
- Used to bypass file type validation

### 3. Race Conditions

Upload validation might have a Time-of-Check-Time-of-Use (TOCTOU) vulnerability:
1. Validate as image
2. **Race window** - rename or modify file
3. Access restricted resources

### 4. Path Traversal

Using special paths to access files outside intended directory:
```
../../../mail/secret.eml
....//....//mail/secret.eml
/mail/secret.eml
```

### 5. Stream Opening Methods

Unix-like systems with special file access:
```bash
# /proc filesystem
/proc/self/environ
/proc/self/fd/

# File descriptor tricks
exec 3< /mail/secret.eml
cat <&3
```

## Incomplete Analysis

This challenge requires:
- [ ] Understanding the exact validation mechanism
- [ ] Identifying which file system/OS is targeted
- [ ] Obtaining/analyzing `download_image` binary
- [ ] Finding the correct bypass technique
- [ ] Accessing `/mail/secret.eml`
- [ ] Extracting the flag

## Related Concepts

- **File Type Detection** - MIME types, magic bytes, file signatures
- **Alternate Data Streams** - NTFS ADS, file attributes
- **Polyglot Files** - Multiple format compatibility
- **Path Traversal** - Directory traversal attacks
- **Race Conditions** - TOCTOU vulnerabilities
- **File Descriptor Manipulation** - Unix file I/O tricks

## Potential Tools

- `file` - Determine file type
- `hexdump` / `xxd` - Inspect binary data
- `strings` - Extract readable strings
- `strace` / `ltrace` - System call tracing
- `binwalk` - Extract files from binaries
- `exiftool` - Inspect metadata

## Next Steps

1. **Analyze** `download_image` binary for clues
2. **Research** the specific attack vector
3. **Test** bypass techniques
4. **Access** `/mail/secret.eml`
5. **Extract** flag from email

## Flag Format

`HQX{...}`

---

**Status:** This challenge remains partially unsolved. Further investigation into the specific bypass technique and challenge interface is required.
