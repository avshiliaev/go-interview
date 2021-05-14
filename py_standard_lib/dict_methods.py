class DictMethods:
    def __init__(self):
        pass

    @staticmethod
    def _from_keys():
        x = ('key1', 'key2', 'key3')
        y = 0

        print(dict.fromkeys(x, y))  # {'key1': 0, 'key2': 0, 'key3': 0}
        print(dict.fromkeys(x))  # {'key1': None, 'key2': None, 'key3': None}

    @staticmethod
    def _get():
        car = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964
        }

        x = car.get("price", 15000)
        print(x)

    @staticmethod
    def _iterate():
        car = {
            "brand": "Ford",
            "model": "Mustang",
            "year": 1964
        }

        for k, v in car.items():
            print(f"{k}:{v}")

    def run(self):
        self._from_keys()
        self._get()
        self._iterate()


if __name__ == '__main__':
    dict_methods = DictMethods()
    dict_methods.run()
