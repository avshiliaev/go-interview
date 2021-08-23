def is_palindrome(self, x: int) -> bool:
    # https://www.javatpoint.com/how-to-reverse-a-number-in-python
    if x < 0:
        return False

    # Initiate value to null
    x_init = x
    x_rev = 0

    # reverse the integer number using the while loop
    while x_init > 0:
        # Logic
        remainder = x_init % 10
        x_rev = (x_rev * 10) + remainder
        x_init = x_init // 10

    return x == x_rev
