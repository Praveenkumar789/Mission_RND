__author__ = 'Kalyan'

notes = '''
1. Read instructions for the function carefully and constraints carefully.
2. Try to generate all possible combinations of tests which exhaustively test the given constraints.
3. If behavior in certain cases is unclear, you can ask on the forums
'''
from placeholders import *

# Convert a sentence which has either or to only the first choice.
# e.g we could either go to a movie or a hotel -> we could go to a movie.
# note: do not use intermediate lists (string.split), only use string functions
# assume words are separated by a single space. you can use control flow statements
# So sentence is of form <blah> either <something> or <somethingelse> and gets converted to <blah> <something>
# if it is not of the correct form, you just return the original sentence.
def prune_either_or(sentence):
    try:
        if type(sentence).__name__ != "str":
            raise TypeError
        E_count = sentence.count(" either")
        O_count = sentence.count(" or")
        if E_count == 1 and O_count == 1 and sentence.find('either') != 0:
            sentence = sentence.replace("either ","")
            if "or" not in sentence:
                raise AttributeError
            or_index = sentence.find(" or")
            sentence = sentence[:or_index]
            return sentence
        else:
            return sentence
    except AttributeError:
        return sentence
    except TypeError:
        pass
def test_prune_either_or_student():
    assert "we could go to a movie" == prune_either_or("we could either go to a movie or a hotel")
    assert  "<blah> <something>" == prune_either_or("<blah> either <something> or <somethingelse>")
    assert "I can write python code" == prune_either_or("I can either write python code or c code")
    assert "is either replaced" == prune_either_or("is either replaced")
    assert "is removed or not removed" == prune_either_or("is removed or not removed")
    assert "We can go to a movie" == prune_either_or("We can go either to a movie or to a hotel")
    assert "We can go either way" == prune_either_or("We can go either way")
    assert "either this or that" == prune_either_or("either this or that")
    assert "neither this nor that" == prune_either_or("neither this nor that")
    assert None == prune_either_or(None)
    assert None == prune_either_or([])
# these tests run only on our runs and will be skipped on your computers.
# DO NOT EDIT.
import pytest
def test_prune_either_or_server():
    servertests = pytest.importorskip("unit5_server_tests")
    servertests.test_prune_either_or(prune_either_or)
