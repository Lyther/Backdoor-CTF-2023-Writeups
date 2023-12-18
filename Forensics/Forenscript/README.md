# Forensics/Forenscript

It's thundering outside and you are you at your desk having solved 4 forensics challenges so far. Just pray to god you solve this one. You might want to know that sometimes too much curiosity hides the flag.

Downloads: [public.zip](./public.zip)

## Solution

Find `a.bin`, seems to be a PNG file with reversed every 4 bytes. Write a script to get the origin image.

```python
content = open('a.bin', 'rb').read()
output = open('b.png', 'wb')
result = []

for i in range(0, len(content), 4):
    for j in range(4):
        result.append(content[i + (3 - j)])

output.write(bytes(result))
```

Below is the `b.png`:

![b.png](./b.png)

Extract using binwalk:

```bash
binwalk --d=".*" b.png
```

We can find the offset `0xEA90` has another image, which is the flag:

![c.png](./c.png)

## Flag

```plaintext
flag{scr1pt1ng_r34lly_t0ugh_a4n't_1t??}
```

