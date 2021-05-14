class StringMethods:
    def __init__(self):
        pass

    @staticmethod
    def _all():
        # capitalize()
        # Converts the first character to upper case

        # casefold()
        # Converts string into lower case

        # center()
        # Returns a centered string

        # count()
        # Returns the number of times a specified value occurs in a string

        # encode()
        # Returns an encoded version of the string
        txt = "My name is Ståle"
        x = txt.encode()
        print(x)  # UTF-8 encode the string

        # endswith()
        # Returns true if the string ends with the specified value

        # expandtabs()
        # Sets the tab size of the string

        # find()
        # Searches the string for a specified value and returns the position of where it was found
        txt = "Hello, welcome to my world."
        x = txt.find("welcome")
        print(x)  # 7

        # format()
        # Formats specified values in a string

        # format_map()
        # Formats specified values in a string

        # index()
        # Searches the string for a specified value and returns the position of where it was found
        txt = "Hello, welcome to my world."
        x = txt.index("welcome")
        print(x)  # 7

        # isalnum()
        # Returns True if all characters in the string are alphanumeric
        txt = "Company12"
        x = txt.isalnum()
        print(x)  # True

        # isalpha()
        # Returns True if all characters in the string are in the alphabet

        # isdecimal()
        # Returns True if all characters in the string are decimals
        txt = "\u0033"  # unicode for 3
        x = txt.isdecimal()
        print(x)  # True

        # isdigit()
        # Returns True if all characters in the string are digits
        txt = "50800"
        x = txt.isdigit()
        print(x)  # True

        # isidentifier()
        # Returns True if the string is an identifier

        # islower()
        # Returns True if all characters in the string are lower case

        # isnumeric()
        # Returns True if all characters in the string are numeric

        # isprintable()
        # Returns True if all characters in the string are printable

        # isspace()
        # Returns True if all characters in the string are whitespaces

        # istitle()
        # Returns True if the string follows the rules of a title

        # isupper()
        # Returns True if all characters in the string are upper case

        # join()
        # Joins the elements of an iterable to the end of the string
        my_tuple = ("John", "Peter", "Vicky")
        x = "#".join(my_tuple)
        print(x)  # John#Peter#Vicky

        # ljust()
        # Returns a left justified version of the string

        # lower()
        # Converts a string into lower case

        # lstrip()
        # Returns a left trim version of the string

        # maketrans()
        # Returns a translation table to be used in translations

        # partition()
        # Returns a tuple where the string is parted into three parts
        # 1 - everything before the "match"
        # 2 - the "match"
        # 3 - everything after the "match"
        txt = "I could eat bananas all day"
        x = txt.partition("bananas")
        print(x)  # ('I could eat ', 'bananas', ' all day')

        # replace()
        # Returns a string where a specified value is replaced with a specified value
        txt = "I like bananas"
        x = txt.replace("bananas", "apples")
        print(x)  # I like apples

        # rfind()
        # Searches the string for a specified value and returns the last position of where it was found
        txt = "Mi casa, su casa."
        x = txt.rfind("casa")
        print(x)  # 12

        # rindex()
        # Searches the string for a specified value and returns the last position of where it was found

        # rjust()
        # Returns a right justified version of the string

        # rpartition()
        # Returns a tuple where the string is parted into three parts

        # rsplit()
        # Splits the string at the specified separator, and returns a list
        txt = "apple, banana, cherry"
        x = txt.rsplit(", ", 1)
        print(x)  # ['apple, banana', 'cherry']

        # rstrip()
        # Returns a right trim version of the string

        # split()
        # Splits the string at the specified separator, and returns a list
        txt = "apple, banana, cherry"
        x = txt.split(", ", 1)
        print(x)  # ['apple', 'banana, cherry']

        # splitlines()
        # Splits the string at line breaks and returns a list

        # startswith()
        # Returns true if the string starts with the specified value

        # strip()
        # Returns a trimmed version of the string
        txt = "     banana     "
        x = txt.strip()
        print("of all fruits", x, "is my favorite")  # of all fruits banana is my favorite

        # swapcase()
        # Swaps cases, lower case becomes upper case and vice versa

        # title()
        # Converts the first character of each word to upper case

        # translate()
        # Returns a translated string

        # upper()
        # Converts a string into upper case

        # zfill()
        # Fills the string with a specified number of 0 values at the beginning
        txt = "50"
        x = txt.zfill(10)
        print(x)  # 0000000050

    def run(self):
        self._all()


if __name__ == '__main__':
    string_methods = StringMethods()
    string_methods.run()
