__author__ = 'Kalyan'

problem = """
Pig latin is an amusing game. The goal is to conceal the meaning of a sentence by a simple encryption.

Rules for converting a word to pig latin are as follows:

1. If word starts with a consonant, move all continuous consonants at the beginning to the end
   and add  "ay" at the end. e.g  happy becomes appyhay, trash becomes ashtray, dog becomes ogday etc.

2. If word starts with a vowel, you just add an ay. e.g. egg become eggay, eight becomes eightay etc.

You job is to write a program that takes a sentence from command line and convert that to pig latin and
print it back to console in a loop (till you hit Ctrl+C).

e.g "There is, however, no need for fear." should get converted to  "Erethay isay, oweverhay, onay eednay orfay earfay."
Note that punctuation and capitalization has to be preserved

You must write helper sub routines to make your code easy to read and write.

Constraints: only punctuation allowed is , and . and they will come immediately after a word and will be followed
by a space if there is a next word. Acronyms are not allowed in sentences. Some words may be capitalized
(first letter is capital like "There" in the above example) and you have to preserve its capitalization in the
final word too (Erethay)
"""

import sys
def Pig_latin(sentence):
    op = []
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for word in sentence.split():
        Word = ''
        end = ''
        flag = 0
        begin = 0
        if word[0].isupper():
            begin = 1
        for i in range(len(word)):
            if word[i].lower() in vowels:
                if word[-1].isalpha():
                    Word += word[i:]
                else:
                    flag = 1
                    Word += word[i:-1]
                break
            else:
                end += word[i].lower()
        Word += end
        Word += 'ay'
        if flag == 1:
            Word += word[-1]
        if begin == 1:
            op.append(Word.capitalize())
        else:
            op.append(Word)
    print(op)
    return op

if __name__ == "__main__":
    sentence = input()
    Pig_latin_text = Pig_latin(sentence)
    while True:
        for word in Pig_latin_text:
            print(word)

    #sys.exit(main())