# Description

Author: @HuskyHacks

HelpfulDesk is the go-to solution for small and medium businesses who need remote monitoring and management. Last night, HelpfulDesk released a security bulletin urging everyone to patch to the latest patch level. They were scarce on the details, but I bet that can't be good...

## Solution

1. Start instance
2. login with admin:admin
3. Check security advisory, and download all three versions of the helpdesk software pkg, i.e 1.1 1.2 1.0
4. extract all and diff, dll and pdb files are different
5. Go recursive now :) using ripgrep, it supports binary level search so `rg flag`
6. A JSON shows a flag.txt under a vm instance
7. Bingo, checkout every machines, flag should be present in second machine under files.
