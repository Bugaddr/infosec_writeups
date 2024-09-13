# Data Vault Duel - 100

**Description**: In a world where data is the new currency, only the best can claim the title of a master infiltrator. Today, you are tasked with a critical mission: to infiltrate a highly secure S3 bucket and retrieve a hidden flag.

**Bucket Name**: `kpmg-ctf1`

## Approach

1. kpmg-ctf1 is a S3 bucket at [https://kpmg-ctf1.s3.amazonaws.com/](https://kpmg-ctf1.s3.amazonaws.com/)
2. Enumerate this with cloud_enum tool.
3. an endpoint has textfile at [https://kpmg-ctf1.s3.amazonaws.com/rituognriteuonhbiorentgbvhuitrhoirtsnbiuort.txt](https://kpmg-ctf1.s3.amazonaws.com/rituognriteuonhbiorentgbvhuitrhoirtsnbiuort.txt) which has flag

### Alternative approach

**Step 1: Accessing the S3 Bucket**

The challenge provided an S3 bucket name `kpmg-ctf1`. To access this bucket, we used the AWS CLI tool with anonymous access since credentials were not required for public access.

```bash
aws s3 ls s3://kpmg-ctf1/ --no-sign-request
```

The output listed two files:

```yaml
2024-07-02 09:05:47          0 index.html
2024-07-02 10:38:09         42 rituognriteuonhbiorentgbvhuitrhoirtsnbiuort.txt
```

**Step 2: Downloading the Files**

To inspect the contents of the bucket, we downloaded the files using the `aws s3 cp` command:

```bash
bashCopy code
aws s3 cp s3://kpmg-ctf1/index.html ./ --no-sign-request
aws s3 cp s3://kpmg-ctf1/rituognriteuonhbiorentgbvhuitrhoirtsnbiuort.txt ./ --no-sign-request
```

**Step 3: Analyzing the Files**

1. **index.html**:
    - We opened this file to check for any relevant information, comments, or hidden clues. However, in this case, `index.html` was empty.
2. **rituognriteuonhbiorentgbvhuitrhoirtsnbiuort.txt**:
    - This file was small, with a size of 42 bytes. Upon opening it, we found the complete flag:

        ```
        KPMG_CTF{cbf35723276f7cd30486971cd1027a79}
        ```
