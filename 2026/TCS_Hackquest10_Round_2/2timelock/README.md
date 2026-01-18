# Challenge 2: Timelock

**Category:** Web / Miscellaneous  
**Difficulty:** Easy  
**Status:** ✅ Solved

## Description

Bypass a web timer that requires hours of simulated elapsed time to proceed.

## Challenge Overview

The webpage implements a timer requiring hours of elapsed time before revealing the flag. The challenge is to simulate the passage of time without actually waiting.

## Vulnerability

The webpage stores elapsed time in browser `localStorage` using client-side JavaScript. This timing mechanism can be trivially bypassed by directly manipulating the storage value.

## Solution

Instead of waiting for hours, directly set the localStorage value to simulate the required elapsed time:

```javascript
localStorage.setItem(
  "timelock_v1_data",
  JSON.stringify({
    elapsed: 12.5 * 60 * 60 * 1000  // 12.5 hours in milliseconds
  })
);
location.reload();
```

## Exploitation Steps

1. Open the challenge webpage in your browser
2. Open Developer Tools (F12)
3. Navigate to the Console tab
4. Paste the JavaScript code above
5. Press Enter to execute
6. The page will reload with simulated elapsed time
7. Flag is now revealed

## Alternative Time Values

Adjust the multiplier as needed:
```javascript
// 24 hours
elapsed: 24 * 60 * 60 * 1000

// 48 hours
elapsed: 48 * 60 * 60 * 1000

// 12 hours
elapsed: 12 * 60 * 60 * 1000
```

## Key Insights

- **Client-side validation is insecure** - Never rely on JavaScript for security
- **localStorage is fully accessible** - Any user can inspect and modify it
- **Timing mechanisms are bypassable** - Time-based checks require server-side enforcement
- **Browser DevTools are powerful** - Exploitation is trivial with proper tools

## Security Lessons

1. All client-side checks can be bypassed
2. Sensitive operations must validate server-side
3. User input (including time) should never be trusted
4. Critical decisions should not depend on client-side timing

## Flag Format

`HQX{...}`
