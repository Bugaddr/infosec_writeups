# Sea Scavenger

foren, 50 points, 589 solves

Take a tour of the deep sea! Explore the depths of webpage secrets and find the hidden treasure. Pro tip: Zoom out!
Resources:
Web servers:
challs.bcactf.com:31314
Categories:
foren, webex
50 points589 solves
Hints:
Press F12 or Ctrl+Shift+I on Windows (Cmd+Option+I on Mac OS) to launch DevTools
Some parts have hints in the console
By pinuna27

## Solution

1. Check js of whale page `Part 5 of the flag: "e4sur3"`
2. Check html of shark page `You found the shark! Part 1 of the flag: "bcactf{b3"`
3. Check developer console of squid page `console.log("You found it! Here's the second part of the flag: \"t_y0u_d1\"");`
4. Check cookies of clam page `flag part 3::"dnt_f1n"`
5. Use curl to check headers of shipwreak page `Flag_Part_4: d_th3_tr`
6. Check robots.txt on treasure page `You found the rest of the flag! _t336e3}`
7. Reconstruct the flag `bcactf{b3t_y0u_d1dnt_f1nd_th3_tre4sur3_t336e3}`
