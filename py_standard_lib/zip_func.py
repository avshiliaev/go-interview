#

class ZipFunctions:

    def __init__(self):
        pass

    @staticmethod
    def _all():

        # zip()
        numbers = [1, 2, 3]
        letters = ['a', 'b', 'c']
        zipped = zip(numbers, letters)  # Holds an iterator object
        print(type(zipped))  # <class 'zip'>
        print(list(zipped))  # [(1, 'a'), (2, 'b'), (3, 'c')]

        s1 = {2, 3, 1}
        s2 = {'b', 'a', 'c'}
        print(list(zip(s1, s2)))  # [(1, 'b'), (2, 'c'), (3, 'a')] UNORDERED pairs

        integers = [1, 2, 3]
        letters = ['a', 'b', 'c']
        floats = [4.0, 5.0, 6.0]
        zipped = zip(integers, letters, floats)  # Three input iterables
        print(list(zipped))  # [(1, 'a', 4.0), (2, 'b', 5.0), (3, 'c', 6.0)]

        # Unequal range
        print(list(zip(range(5), range(100))))  # [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]

        # Iterate over multiple values
        letters = ['a', 'b', 'c']
        numbers = [0, 1, 2]
        operators = ['*', '/', '+']
        for l, n, o in zip(letters, numbers, operators):
            print(f'Letter: {l}')
            print(f'Number: {n}')
            print(f'Operator: {o}')

        # The same with dicts
        dict_one = {'name': 'John', 'last_name': 'Doe', 'job': 'Python Consultant'}
        dict_two = {'name': 'Jane', 'last_name': 'Doe', 'job': 'Community Manager'}
        for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
            print(k1, '->', v1)
            print(k2, '->', v2)

        # Build a dict
        fields = ['name', 'last_name', 'age', 'job']
        values = ['John', 'Doe', '45', 'Python Developer']
        a_dict = dict(zip(fields, values))
        print(a_dict)  # {'name': 'John', 'last_name': 'Doe', 'age': '45', 'job': 'Python Developer'}

        new_job = ['Python Consultant']
        field = ['job']
        a_dict.update(zip(field, new_job))
        print(a_dict)  # {'name': 'John', 'last_name': 'Doe', 'age': '45', 'job': 'Python Consultant'}

        # Unzip
        from_pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
        numbers, letters = zip(*from_pairs)  # (1, 2, 3, 4), ('a', 'b', 'c', 'd')

        from_list = ["00", "11", "22", "33"]
        print(list(zip(*from_list)))  # [('0', '1', '2', '3'), ('0', '1', '2', '3')]

        from_dict = {'name': 'John', 'last_name': 'Doe', 'job': 'Python Consultant'}
        print(list(zip(*from_dict.items())))  # [('name', 'last_name', 'job'), ('Jane', 'Doe', 'Community Manager')]

    def run(self):
        self._all()


if __name__ == '__main__':
    built_ins = ZipFunctions()
    built_ins.run()
