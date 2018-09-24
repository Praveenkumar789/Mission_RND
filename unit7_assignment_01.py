__author__ = 'Kalyan'

problem = """
 We are going to revisit unit6 assignment3 for this problem.

 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 This program should be written as a command line script. It takes one argument the input file of words and outputs
 <input>-results.txt where <input>.txt is the input file of words.
"""
import sys
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
    ds_file = open(destination, 'w')
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
if __name__ == "__main__":
    import unit6utils
    source = unit6utils.get_input_file("unit6_testinput_03.txt")
    destination = unit6utils.get_temp_file("unit6_output_03.txt")
    anagram_sort(source, destination)
    #sys.exit(main())