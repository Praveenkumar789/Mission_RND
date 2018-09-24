_author__ = 'Kalyan'

notes = '''
Now we move on to writing both the function and the tests yourself.

In this assignment you have to write both the tests and the code. We will verify your code against our own tests
after you submit.
'''

# fill up this routine to test if the 2 given words given are anagrams of each other. http://en.wikipedia.org/wiki/Anagram
# your code should handle
#  - None inputs
#  - Case  (e.g Tip and Pit are anagrams)
def are_anagrams(first, second):
    try:
        check = {}
        assert type(first).__name__ == 'str' or type(first).__name__ == 'str'
        assert len(first) == len(second)
        for letter in first.lower():
            if letter not in check.keys():
                check[letter] = 1
            else:
                check[letter] += 1
        for letter in second.lower():
            check[letter] -= 1
        return list(check.values()) == [0 for i in range(len(set(first.lower())))]
    except TypeError as te:
        return False
    except AttributeError:
        return False
    except AssertionError:
        return False
    except KeyError:
        return False

# write your own exhaustive tests based on the spec given
def test_are_anagrams_student():
    assert True == are_anagrams("pit", "tip") #sample test.
    assert False == are_anagrams("Cat", "Dog")
    assert True == are_anagrams("Tap", "apt")
    assert False == are_anagrams("Good","God")
    assert False == are_anagrams(None, "Hi")
    assert False == are_anagrams("Hello", None)
    assert False == are_anagrams(None, None)
    assert True == are_anagrams("Alphabets", "phalatebs")
    assert True == are_anagrams("Morning", "GNINROM")
    assert True == are_anagrams("AABB CC","ccbbaa ")
    assert False == are_anagrams(None, None)
    assert False == are_anagrams(None, "hello")
    assert False == are_anagrams("hello", None)
    assert False == are_anagrams("bigg", "big")
    assert False == are_anagrams("bigg", "biig")
test_are_anagrams_student()
# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_are_anagrams_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_are_anagrams(are_anagrams)
