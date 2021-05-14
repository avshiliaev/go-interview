class SetMethods:

    def __init__(self):
        pass

    @staticmethod
    def _all():
        # add()
        # Adds an element to the set
        fruits = {"apple", "banana", "cherry"}
        fruits.add("orange")

        # difference()
        # Returns a set containing the difference between two or more sets
        x = {"apple", "banana", "cherry"}
        y = {"google", "microsoft", "apple"}
        z = x.difference(y)
        print(z)  # {'cherry', 'banana'}

        # difference_update()
        # Removes the items in this set that are also included in another, specified set
        x = {"apple", "banana", "cherry"}
        y = {"google", "microsoft", "apple"}
        x.difference_update(y)
        print(x)  # {'cherry', 'banana'}

        # discard()
        # Remove the specified item

        # intersection()
        # Returns a set, that is the intersection of two other sets
        x = {"apple", "banana", "cherry"}
        y = {"google", "microsoft", "apple"}
        z = x.intersection(y)
        print(z)  # {'apple'}

        # intersection_update()
        # Removes the items in this set that are not present in other, specified set(s)
        x = {"apple", "banana", "cherry"}
        y = {"google", "microsoft", "apple"}
        x.intersection_update(y)
        print(x)  # {'apple'}

        # isdisjoint()
        # Returns whether two sets have a intersection or not
        x = {"apple", "banana", "cherry"}
        y = {"google", "microsoft", "facebook"}
        z = x.isdisjoint(y)
        print(z)  # True

        # issubset()
        # Returns whether another set contains this set or not
        x = {"a", "b", "c"}
        y = {"f", "e", "d", "c", "b", "a"}
        z = x.issubset(y)
        print(z)  # True

        # issuperset()
        # Returns whether this set contains another set or not
        x = {"f", "e", "d", "c", "b", "a"}
        y = {"a", "b", "c"}
        z = x.issuperset(y)
        print(z)  # True

        # pop()
        # Removes an element from the set

        # remove()
        # Removes the specified element

        # symmetric_difference()
        # Returns a set with the symmetric differences of two sets
        x = {"apple", "banana", "cherry"}
        y = {"google", "microsoft", "apple"}
        z = x.symmetric_difference(y)
        print(z)  # {'google', 'banana', 'cherry', 'microsoft'}

        # symmetric_difference_update()
        # inserts the symmetric differences from this set and another

        # union()
        # Return a set containing the union of sets
        x = {"apple", "banana", "cherry"}
        y = {"google", "microsoft", "apple"}
        z = x.union(y)
        print(z)  # {'microsoft', 'apple', 'google', 'banana', 'cherry'}

        # update()
        # Update the set with another set, or any other iterable
        x = {"apple", "banana", "cherry"}
        y = ["google", "microsoft", "apple"]
        x.update(y)
        print(x)  # {'cherry', 'apple', 'banana', 'microsoft', 'google'}

    def run(self):
        self._all()


if __name__ == '__main__':
    set_methods = SetMethods()
    set_methods.run()
