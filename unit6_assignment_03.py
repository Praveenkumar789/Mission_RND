__author__ = 'Kalyan'

notes = '''
 This problem will require you to put together many things you have learnt
 in earlier units to solve a problem.

 In particular you will use functions, nested functions, file i/o, functions, lists, dicts, iterators, generators,
 comprehensions,  sorting etc.

 Read the constraints carefully and account for all of them. This is slightly
 bigger than problems you have seen so far, so decompose it to smaller problems
 and solve and test them independently and finally put them together.

 Write subroutines which solve specific subproblems and test them independently instead of writing one big
 mammoth function.

 Do not modify the input file, the same constraints for processing input hold as for unit6_assignment_02
'''

problem = '''
 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 source - file containing words, one word per line, some words may be capitalized, some may not be.
 - read words from the source file.
 - group them into anagrams. how?
 - sort each group in a case insensitive manner
 - sort these groups by length (desc) and in case of tie, the first word of each group
 - write out these groups into destination
'''

import unit6utils
import string
l = [1,2,3]

def anagram_sort(source, destination):
    def is_anagram(word1, word2):
        check = {}
        if len(word1) != len(word2):return False
        for letter in word1:
            if letter not in check.keys():
                check[letter] = 1
            else:
                check[letter] += 1
        for letter in word2:
            if letter in check.keys():
                check[letter] -= 1
        if sum(list(check.values())) == 0:
            return True
        return False
    sr_file = open(source, 'r')
    ds_file = open(destination, 'r+')
    Anagram_dict = {}
    Main_words = [word.strip() + '\n' for word in sr_file.readlines() if word[0] != ' ' and word[0] != '#' and word[0] != '\n']
    while len(Main_words) != 0:
        words = Main_words
        I = Main_words[0]
        Anagram_dict[I] = [I]
        for word in words[1:]:
            if is_anagram(I.lower(),word.lower()):
                Anagram_dict[I].append(word)
                Main_words.remove(word)
        Main_words.remove(I)
    output = [tuple(sorted(x, key= lambda x:x.lower())) for x in Anagram_dict.values()]
    output.sort(key = lambda x:x[0].lower())
    output.sort(key=lambda x:len(x), reverse = True)
    result = [word for Tuple in output for word in Tuple]
    ds_file.truncate()
    ds_file.writelines(result)
    ds_file.close()

def test_anagram_sort():
    source = unit6utils.get_input_file("unit6_testinput_03.txt")
    expected = unit6utils.get_input_file("unit6_expectedoutput_03.txt")
    destination = unit6utils.get_temp_file("unit6_output_03.txt")
    anagram_sort(source, destination)
    result = [word.strip() for word in open(destination)]
    expected = [word.strip() for word in open(expected)]
    assert expected == result
