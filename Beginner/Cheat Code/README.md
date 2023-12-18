# Beginner/Cheat Code

Enough of Cheat Codesss , this is no GTA SA where you can win using Cheats.Let's see if you can win without it......

Downloads: [public.zip](./public.zip)

## Solution

Reverse the code, and find the verify logic and the first 16 bytes of flag:

```c
__int64 __fastcall fun_1(const char *a1, __int64 a2)
{
  int i; // [rsp+18h] [rbp-28h]
  int j; // [rsp+1Ch] [rbp-24h]
  __int64 v5[4]; // [rsp+20h] [rbp-20h] BYREF

  v5[3] = __readfsqword(0x28u);
  if ( strlen(a1) == 32 )
  {
    for ( i = 0; i <= 15; ++i )
    {
      if ( *(_DWORD *)(4LL * i + a2) != (char)(a1[i] ^ a1[31 - i]) )
      {
        puts("That's quite a noob thing u did ^.^ ");
        return 0LL;
      }
    }
    qmemcpy(v5, "flag{c4n't_HESOY", 16);
    for ( j = 0; j <= 15; ++j )
    {
      if ( a1[j] != *((_BYTE *)v5 + j) )
      {
        puts("That's quite a noob thing u did ^.^ ");
        return 0LL;
      }
    }
    return 1LL;
  }
  else
  {
    puts("Just open the file first");
    return 0LL;
  }
}
```

Write reverse code to decrypt the verification:

```c
#include <stdio.h>

int main() {
    char v4[16] = {27, 25, 81, 30, 36, 13, 0, 13, 120, 65, 110, 32, 114, 12, 2, 24};
    char v5[16] = "flag{c4n't_HESOY";
    char v6[16] = "xxxxxxxxxxxxxxxx";

    for (int i = 0; i < 16; i++) {
        char result = (char)(*(i+v4) ^ v5[i]);
        printf("%c ", result);
        v6[15-i] = result;
    }
    printf("\n");
    for (int i = 0; i < 16; i++) {
        printf("%c", v5[i]);
    }
    for (int i = 0; i < 16; i++) {
        printf("%c", v6[i]);
    }
    return 0;
}
```

## Flag

```plaintext
flag{c4n't_HESOYAM_7h15_c4n_y0u}
```

