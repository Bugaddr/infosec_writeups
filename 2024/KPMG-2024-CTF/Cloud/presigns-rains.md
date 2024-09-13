# Presign Rains

### 1. Initial Reconnaissance

- **Accessing the URL**: The first step was to visit the provided URL. Using `curl` to retrieve the page revealed that it was redirected to an HTTPS version:

    ```bash
    curl -i http://kicyber2024-a1400bb0e2ce-presign-1.chals.io
    ```

    The page was successfully accessed via HTTPS.

- **Inspecting the Page Content**: The HTML content of the page contained hidden information in white text, indicating an AWS Access Key and a bucket name:

    ```html
    htmlCopy code
    <p style="color: white;">Presign rains here: AKIA33VJAWOZJLLBCU2A</p>
    <p style="color: white;">Presign rain collects in this bucket: ctf2k24-best</p>
    ```

### 2. Analyzing `robots.txt`

- **Exploring `robots.txt`**: A `robots.txt` file was found that provided further clues. It contained several paths:One of the paths (`/robot`) led to a URL template.

    ```bash
    bashCopy code
    /5625d8f847a29410e05b91df5628d6d2fa8146eed792c0ae048279798853d1b9
    /604800
    /20240808T094405Z
    /robot
    /us-east-1
    ```

### 3. Constructing the Pre-signed URL

- **Identifying the Components**: Using the information provided:
  - Bucket name: `ctf2k24-best`
  - AWS Access Key: `AKIA33VJAWOZJLLBCU2A`
  - Region: `us-east-1`
  - Date: `20240808T094405Z`
  - Expiry Time: `604800`
  - Signature: `5625d8f847a29410e05b91df5628d6d2fa8146eed792c0ae048279798853d1b9`
- **URL Construction**: The pre-signed URL was constructed as follows:

    ```bash
    bashCopy code
    https://ctf2k24-best.s3.us-east-1.amazonaws.com/flag.txt?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA33VJAWOZJLLBCU2A%2F20240808%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240808T094405Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=5625d8f847a29410e05b91df5628d6d2fa8146eed792c0ae048279798853d1b9
    ```

### 4. Discovering the Final Flag

- **URL Access**: After constructing the URL, it was accessed, revealing that the path `/1tr41n5pr3_s1gn3d_UrL5_he73_4nd_T4kE3_y0uR_F1a9` was actually a directory leading to the final flag.
- **Final Flag Retrieval**: By navigating to the directory:The flag was successfully retrieved:

    ```bash
    bashCopy code
    https://kicyber2024-a1400bb0e2ce-presign-1.chals.io/1tr41n5pr3_s1gn3d_UrL5_he73_4nd_T4kE3_y0uR_F1a9/
    ```
