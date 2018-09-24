__author__ = 'Kalyan'

notes = '''
These are the kind of questions that are typically asked in written screening tests by companies,
so treat this as practice!

Convert the passed in positive integer number into its prime factorization form.

If number = a1 ^ p1 * a2 ^ p2 ... where a1, a2 are primes and p1, p2 are powers >=1 then we represent that using lists
and tuples in python as [(a1,p1), (a2,p2), ...]

Note that a1 < a2 < ... and p1, p2 etc are all >= 1.

For e.g.
 [(2,1), (5,1)] is the correct prime factorization of 10 as defined above.
 [(5,1), (2,1)] is invalid as the the order is not correct.
 [(2,1), (3,0), (5,1)] is invalid as a prime with power 0 is present in the result.

Notes
0. This problems asks for explicit type checking!
1. Corner case 1 is represented as an empty list: []
2. Non positive numbers should raise a ValueError
3. If the type of number is not int raise a TypeError

Write simple brute force code. No need to write code for generating primes etc.
'''

def factorize_number(number):
    def isprime(Num):
        if Num < 2:
            return False
        else:
            count = 0
            for i in range(1,Num):
                if Num % i == 0:
                    count += 1
            return count == 2
    try:
        if number < 0:
            raise ValueError
        else:
            if number == 1:
                return []
        if type(number).__name__ != 'int':
            raise TypeError
        factorize_Dict = {}
        Num = number
        count = 0
        while Num % 2 == 0:
            count += 1
            factorize_Dict[2] = count
            Num = Num // 2
        divisor = 3
        while divisor  < int(Num ** (1/2)):
            count = 0
            while Num % divisor == 0:
                count += 1
                factorize_Dict[divisor] = count
                Num = Num // divisor
            divisor += 2
        if Num > 2:
            factorize_Dict[Num] = 1

        return list(zip(factorize_Dict.keys(), factorize_Dict.values()))

    except ValueError as ve:
        print(ve)

    except TypeError as Te:
        print(Te)

# you are given the tests here according to the spec, usually you will have to write these yourself from the spec!
def test_factorize_number():
    assert [] == factorize_number(1)
    assert [(2, 3), (3,1)] == factorize_number(24)
    assert [(2, 1), (5, 1), (601, 1)] == factorize_number(6010)
    assert [(5, 2), (7, 1)] == factorize_number(175)
    assert [(2, 1), (7919, 4)] == factorize_number(7865228921869442)
    try:
        factorize_number(-3)
        assert True, "negative number did not throw"
    except ValueError as ve:
        pass

    try:
        factorize_number(2.3)
        assert True, "float did not throw"
    except TypeError as te:
        pass
