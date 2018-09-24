__author__ = 'Kalyan'

notes = '''
Write your own implementation of converting a number to a given base. It is important to have a good logical
and code understanding of this.

Till now, we were glossing over error checking, for this function do proper error checking and raise exceptions
as appropriate.

Reading material:
    http://courses.cs.vt.edu/~cs1104/number_conversion/convexp.html
'''

def convert(number, base):
    """
    Convert the given number into a string in the given base. valid base is 2 <= base <= 36
    raise exceptions similar to how int("XX", YY) does (play in the console to find what errors it raises).
    Handle negative numbers just like bin and oct do.
    """
    try:
        import string
        Num = number
        flag = 0
        Converted_str = []
        if type(number).__name__  != 'int' or type(base).__name__ != 'int':
            raise TypeError
        if not (1 < base and base < 37):
            raise ValueError
        if number < 0:
            Num = abs(number)
            flag = 1
        while True:
            rem = Num%base
            Converted_str.append(rem)
            Num = Num // base
            if Num < base:
                Converted_str.append(Num)
                break
        Converted_str.reverse()
        Numers = list(range(10,37))
        After_9 = dict(zip(Numers,string.ascii_uppercase))
        for i in range(len(Converted_str)):
                if Converted_str[i] > 9:
                    Converted_str[i] = After_9[Converted_str[i]]
                else:
                    Converted_str[i] = str(Converted_str[i])
        Str_Form = "".join(Converted_str)
        if flag == 1:
            return "-"+Str_Form
        return Str_Form

    except ValueError as  Ve:
        print(Ve)

    except TypeError as Te:
        print(Te)

def test_convert():
    assert "100" == convert(4,2)
    assert "FF" == convert(255,16)
    assert "377" == convert(255, 8)
    assert "JJ" == convert(399, 20)
    assert "-JJ" == convert(-399, 20)

    try:
        convert(10,1)
        assert True,"Invalid base <2 did not raise error"
    except ValueError as ve:
        print(ve)

    try:
        convert(10, 40)
        assert True, "Invalid base >36 did not raise error"
    except ValueError as ve:
        print(ve)

    try:
        convert("100", 10)
        assert True, "Invalid number did not raise error"
    except TypeError as te:
        print(te)

    try:
        convert(None, 10)
        assert True, "Invalid number did not raise error"
    except TypeError as te:
        print(te)


    try:
        convert(100, "10")
        assert True, "Invalid base did not raise error"
    except TypeError as te:
        print(te)
