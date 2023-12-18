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