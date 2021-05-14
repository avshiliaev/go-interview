#

class BuiltInFunctions:

    def __init__(self):
        pass

    @staticmethod
    def _bytes():
        # The bytearray() function is used converts an object into bytearray objects.
        bytearray_ = bytearray(22)
        print(bytearray_)
        # output = bytearray(b'\x00\x00\x00\x00\x00\.....

        # The bytes() function is used to convert objects into bytes object.
        bytes_ = bytes(22)
        print(bytes_)
        # output: b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\......

    @staticmethod
    def _numerics():
        # The abs() function in Python get the positive (absolute) value of a numerical value.
        x = abs(-7.25)
        print(x)
        # output = 7.25

        # The bin() function converts an integer (number) to a binary string. It prefixed with 0b.
        a = bin(30)
        print(a)
        # output = 0b11110

        # divmod() Gets a tuple including the quotient and remainder when argument1 is divided by argument2.
        b = divmod(6, 2)
        print(b)
        # output = (3, 0)

        # round()
        # Rounds a numbers
        x = round(5.76543, 2)
        print(x)  # 5.77

    @staticmethod
    def _booleans():
        # The all() function in python checks if all the items of an iterable are true, else it returns False.
        li = [0, 2, 2]
        a = all(li)
        print(a)
        # output = 7.25

        # The any() function returns True if any item in an iterable is true, else it returns False.
        tup = (0, 1, False)
        a = any(tup)
        print(a)
        # output = True

    @staticmethod
    def _strings():
        # The ascii() replaces non-ascii characters with escape characters.
        a = ascii("Mostly Såne")
        print(a)
        # output = 'Mostly S\xe5ne'

        # The chr() function gets the string character, which represents the defined unicode.
        a = chr(87)
        print(a)
        # output: W

    @staticmethod
    def _iterables():
        # reversed()
        alphas = ["a", "b", "c", "d"]
        ralph = reversed(alphas)
        for x in ralph:
            print(x)

        # map()
        def my_func(n):
            return len(n)

        x = map(my_func, ('apple', 'banana', 'cherry'))
        print(list(x))  # [5, 6, 6]

    def run(self):
        self._bytes()
        self._numerics()
        self._booleans()
        self._strings()
        self._iterables()


if __name__ == '__main__':
    built_ins = BuiltInFunctions()
    built_ins.run()
