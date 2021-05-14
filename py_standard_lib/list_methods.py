class ListMethods:

    @staticmethod
    def _merging_lists_and_elements():
        li = ['Mathematics', 'chemistry', 1997, 2000]
        # Insert at index 2 value 10087
        print(li.insert(2, 10087))

        li1 = [1, 2, 3]
        li2 = [2, 3, 4, 5]
        # Add List2 to List1
        print(li1.extend(li2))

    @staticmethod
    def _aggregations():
        li = [1, 2, 3, 4, 5]

        print(sum(li))
        print(min(li))
        print(max(li))
        print(li.count(1))
        print(li.index(2))

    def run(self):
        self._merging_lists_and_elements()
        self._aggregations()


class ListSortMethods:
    def __init__(self):
        pass

    @staticmethod
    def _sort_asc():
        # vowels list
        vowels = ['e', 'a', 'u', 'o', 'i']

        # sort the vowels
        vowels.sort()

        # print vowels
        print('Sorted list:', vowels)

    @staticmethod
    def _sort_desc():
        # vowels list
        vowels = ['e', 'a', 'u', 'o', 'i']

        # sort the vowels
        vowels.sort(reverse=True)

        # print vowels
        print('Sorted list (in Descending):', vowels)

    @staticmethod
    def _sort_with_key():
        # take second element for sort
        # random list
        random = [(2, 2), (3, 4), (4, 1), (1, 3)]

        # sort list with key
        random.sort(key=lambda x: x[1])

        # print list
        print('Sorted list with key:', random)

    @staticmethod
    def _sort_with_key_lambda():
        # sorting using custom key
        employees = [
            {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
            {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
            {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
            {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
        ]

        # sort by name (Ascending order)
        employees.sort(key=lambda x: x.get('Name'))
        print(employees, end='\n\n')

    def run(self):
        self._sort_asc()
        self._sort_desc()
        self._sort_with_key()


if __name__ == '__main__':
    list_methods = ListSortMethods()
    list_methods.run()
