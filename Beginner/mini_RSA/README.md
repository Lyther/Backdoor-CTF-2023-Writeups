# Beginner/mini_RSA

Groot is stuck on a spaceship somewhere, he wants to send a message to his team so he can get saved but doesn't want anyone in between to read it. So he encrypts the message and then sends it. Now other guardians are unable to understand it, please help them in knowing what's the message.

Downloads: [output.txt](./output.txt), [script.py](./script.py)

## Solution

Small exponential attack on RSA for `e=3`.

```python
from sage.all import ZZ


def attack(e, c):
    """
    Recovers the plaintext from a ciphertext, encrypted using a very small public exponent (e.g. e = 3).
    :param e: the public exponent
    :param c: the ciphertext
    :return: the plaintext
    """
    return int(ZZ(c).nth_root(e))


c=5926440800047066468184992240057621921188346083131741617482777221394411358243130401052973132050605103035491365016082149869814064434831123043357292949645845605278066636109516907741970960547141266810284132826982396956610111589
e=3

print(attack(e, c))
```

Output:

```plaintext
180966415225574282617174341961062752467138759979771496553740193686860546429
```

Use `long_to_bytes` in `Crypto.Util.number` to decrypt.

## Flag

```plaintext
flag{S0_y0u_c4n_s0lv3_s0m3_RSA}
```

