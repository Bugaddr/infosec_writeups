# IDoor (50pts)
Author: @JohnHammond#6971

It's Apple's latest innovation, the "iDoor!" ... well, it is basically the Ring Doorbell camera, but the iDoor offers a web-based browser to monitor your camera, and super secure using ultimate cryptography with even SHA256 hashing algorithms to protect customers! Don't even think about snooping on other people's cameras!! 

# Solution
1. Every url ends with some kind of hash, verifying it with hash analyzer shows that its SHA256.
e.g `http://example.com/site/4fc82b26aecb47d2868c4efbe3581732a3e7cbcc6c2efb32062c08170a05eeb8` and it shows user as 11, sha256 of 11 is 4fc82b26aecb47d2868c4efbe3581732a3e7cbcc6c2efb32062c08170a05eeb8 (`echo -n 11|sha256sum`).
2. So this seems like IDOR, now we will check all the sites, `http://example.com/`(sha256 from 0 to 11) using burp site payload maker by processing the end part as SHA2-256.
3. Flag at `http://example.com/site/5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9` e.g user 0