# Rev/Open Sesame

Whisper the phrase, unveil with 'Open Sesame

Attachment: https://staticbckdr.infoseciitr.in/opensesame.zip

## Solution

Use `jadx` to reverse apk.

Get the following key value:

```java
private static final int[] valid_password = {52, 108, 49, 98, 97, 98, 97};
String trim2 = "4l1baba";
sh4dy(trim2) = 41;
String str = sl4y3r(sh4dy(trim2)) = "40";
String str2 = "U|]rURuoU^PoR_FDMo@X]uBUg";
```

The reverse part of Java is:

```java
private String flag(String str, String str2) {
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < str2.length(); i++) {
        sb.append((char) (str2.charAt(i) ^ str.charAt(i % str.length())));
    }
    return sb.toString();
}
```

Write script in Python:

```python
str1 = "40"
str2 = "U|]rURuoU^PoR_FDMo@X]uBUg"
for i in range(len(str2)):
    print(chr(ord(str2[i])^ord(str1[i%len(str1)])), end='')
```

## Flag

```plaintext
flag{aLiBabA_and_forty_thiEveS}
```

