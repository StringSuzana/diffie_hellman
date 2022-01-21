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
        actual_set = set()  # Here set is used so that only unique numbers should fall in
        for power in range(1, modulo):  # We are searching for a number that will be co-prime
            actual_set.add(pow(co_prime_of_modulo, power, modulo))  # co_prime_of_modulo ^ power % modulo
        if required_set == actual_set:
            return co_prime_of_modulo
        else:
            continue


'''
p=7
g=3

3^0(mod 7) = 1 
3^1(mod 7) = 3  => We are starting from here
3^2(mod 7) = 2
3^3(mod 7) = 6
3^4(mod 7) = 4
3^5(mod 7) = 5 => We end here

What we got? ==>                    primitive root modulo p = 3
Why are we searching for that? ==>  public keys and shared secret can be of any value from 1 to p-1 
Private keys will become exponents!

3^6(mod 7) = 1
3^7(mod 7) = 3
3^8(mod 7) = 2
3^9(mod 7) = 6
3^10(mod 7) = 4
'''


def what_is_primitive_root_modulo_p():
    modulo = 7
    range_of_search = range(1, modulo)  # [1, modulo>
    for possible_root in range_of_search:
        for exponent in range_of_search:
            result = pow(possible_root, exponent, modulo)
            print(f'{possible_root}^{exponent}(mod {modulo}) = {result}')


if __name__ == '__main__':
    what_is_primitive_root_modulo_p()
    # Generating private keys
    alice_private = randint(100, 99999)
    print('Alice private key is %d' % alice_private)
    bob_private = randint(100, 99999)
    print('Bob private key is %d' % bob_private)

    # Generating p-g parameters
    p = get_random_prime()  # p has to be prime nuber
    g = primitive_root(p)  # g has to be primitive root modulo p

    print('\n p parameter is %d, g parameter is %d \n' % (p, g))

    # Generating public keys
    alice_public = pow(g, alice_private) % p
    bob_public = pow(g, bob_private) % p

    print('Alice public key is %d' % alice_public)
    print('Bob public key is %d' % bob_public)

    alice_key = (pow(bob_public, alice_private)) % p
    bob_key = (pow(alice_public, bob_private)) % p

    print('\n Common secret: %d == %d' % (alice_key, bob_key))
