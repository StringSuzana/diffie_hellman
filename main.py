from random import getrandbits
from random import randint


def is_prime(num):
    if num > 1:
        for n in range(2, num):
            if (num % n) == 0:
                return False
        return True
    else:
        return False


def get_random_prime():
    while True:
        n = getrandbits(15);
        if is_prime(n):
            return n


def primitive_root(modulo):
    required_set = set(num for num in range(1, modulo))
    for co_prime_of_modulo in range(1, modulo):
        actual_set = set()
        for power in range(1, modulo):
            actual_set.add(pow(co_prime_of_modulo, power) % modulo)
        if required_set == actual_set:
            return co_prime_of_modulo
        else:
            continue


if __name__ == '__main__':
    # Generating private keys
    alice_private = randint(100, 99999)
    print('Alice private key is %d' % alice_private)
    bob_private = randint(100, 99999)
    print('Bob private key is %d' % bob_private)

    # Generating p-g parameters
    p = get_random_prime()  # p has to be prime nuber
    g = primitive_root(p)  # g has to be primitive rood modulo p

    print('\n p parameter is %d, g parameter is %d \n' % (p, g))

    # Generating public keys
    alice_public = pow(g, alice_private) % p
    bob_public = pow(g, bob_private) % p

    print('Alice public key is %d' % alice_public)
    print('Bob public key is %d' % bob_public)

    alice_key = (pow(bob_public, alice_private)) % p
    bob_key = (pow(alice_public, bob_private)) % p

    print('\n Common secret: %d == %d' % (alice_key, bob_key))
