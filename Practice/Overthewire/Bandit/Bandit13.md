# Bandit 13

```bash
cp * $(mktemp -d)
xxd -r data.txt >>./out.gz
gzip -d out.gz
bzip2 -d out
tar -xf out.out
tar -xf data5.bin
bzip2 -d data6.bin
tar -xf data6.bin.out
mv data8.bin data8.bin.gz
gzip -d data8.bin.gz
cat data8.bin
```
