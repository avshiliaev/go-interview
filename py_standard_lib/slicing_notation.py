class SlicingNotation:

    def __init__(self):
        pass

    @staticmethod
    def _all():
        a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        # a[start:stop]  # items start through stop-1
        # a[start:]  # items start through the rest of the array
        # a[:stop]  # items from the beginning through stop-1
        # a[:]  # a copy of the whole array

        print(a[-1])  # last item in the array
        print(a[-2:])  # last two items in the array
        print(a[:-2])  # everything except the last two items

        print(a[::-1])  # all items in the array, reversed
        print(a[1::-1])  # the first two items, reversed
        print(a[:-3:-1])  # the last two items, reversed
        print(a[-3::-1])  # everything except the last two items, reversed

    def run(self):
        self._all()


if __name__ == '__main__':
    SlicingNotation().run()
