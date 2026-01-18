# Challenge 3: Quietlock

**Category:** Network Forensics  
**Difficulty:** Medium  
**Status:** ✅ Solved

## Description

Analyze a network packet capture to discover hidden DNS-over-HTTPS communications.

## Files

- `42beBe5691.pcap` - Network packet capture file
- `wireshark_filter` - Wireshark filter syntax for identifying relevant traffic
- `aianswer` - Analysis notes

## Solution

Use Wireshark to filter for POST requests to DNS providers, which may hide command-and-control communications.

## Wireshark Filter

```
http.request.method == "POST" && http.host == "dns.google"
```

This filter identifies:
- **http.request.method == "POST"** - Only POST requests (data exfiltration)
- **http.host == "dns.google"** - Requests to Google's DNS server

## Analysis Steps

1. **Open the PCAP file:**
   ```bash
   wireshark 42beBe5691.pcap
   ```

2. **Apply the filter** in the Wireshark filter bar:
   ```
   http.request.method == "POST" && http.host == "dns.google"
   ```

3. **Examine POST data** in the Packet Details pane
4. **Extract DNS-over-HTTPS payload** from the request body
5. **Decode the hidden communication** to retrieve the flag

## Key Observations

- DNS-over-HTTPS can tunnel arbitrary data
- POST requests to DNS servers are suspicious
- Filtering suspicious traffic reveals anomalies
- DNS traffic analysis is critical for detecting C&C communications

## Related Concepts

- **DNS Tunneling** - Hiding data in DNS queries/responses
- **DNS-over-HTTPS (DoH)** - Encrypted DNS for privacy (or covert comms)
- **Network Indicators of Compromise (IoCs)** - Identifying malicious patterns
- **Packet Analysis** - Manual inspection of network traffic

## Lessons Learned

1. Not all DNS is innocent - can hide malicious communications
2. POST to DNS servers is highly suspicious
3. Proper filtering reveals patterns in large captures
4. Network forensics requires understanding protocol layers

## Flag Format

`HQX{...}`
