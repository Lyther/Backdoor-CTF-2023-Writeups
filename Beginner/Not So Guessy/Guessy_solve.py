from pwn import *

context.log_level = 'debug'

Secret_Number = 985508773
how_to_win = {2:'Rock', 1:'Scissors', 0:'Paper'}

p = remote('34.70.212.151', 8010)

while Secret_Number:
    hand = how_to_win[Secret_Number % 3]
    Secret_Number//=3
    p.sendlineafter(b'Rock, Paper, Scissors!', hand.encode())

p.interactive()