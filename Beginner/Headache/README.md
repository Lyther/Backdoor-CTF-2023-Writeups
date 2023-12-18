# Beginner/Headache

I've had a headache since last evening. Is there a magic spell that can cure it immediately?

Downloads: [public.zip](./public.zip)

## Solution

Change the first 8 bytes to PNG file header:

```hex
89 50 4E 47 0D 0A 1A 0A
```

Get this picture:

![chal_fix.png](./chal_fix.png)

## Flag

```plaintext
flag{sp3ll_15_89_50_4E_47}
```

