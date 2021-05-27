import random

if __name__ == '__main__':
    # 1. List Comprehensions with conditionals
    # new_list = [expression for member in iterable (if conditional)]
    sentence = 'the rocket came back from mars'
    vowels = [i for i in sentence if i in 'aeiou']

    # The conditional can test any valid expression.
    sentence = 'The rocket, who was named Ted, came back from Mars because he missed his friends.'
    consonants = [i for i in sentence if i.isalpha() and i.lower() not in vowels]

    # new_list = [expression (if conditional) for member in iterable]
    original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
    prices = [i if i > 0 else 0 for i in original_prices]

    # NESTED
    vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flat_vector = [number for li in vector for number in li]
    # [1, 2, 3, 4, 5, 6, 7, 8, 9]

    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix))]
    # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    # 2. Set and Dictionary Comprehensions
    # Set
    quote = "life, uh, finds a way"
    unique_vowels = {i for i in quote if i in 'aeiou'}

    # 3. Dictionary
    squares = {i: i * i for i in range(10)}

    # NESTED
    dict_ = {(k, v): k + v for k in range(2) for v in range(2)}
    # {(0, 1): 1, (1, 0): 1, (0, 0): 0, (1, 1): 2}

    # 4. Walrus Operator
    hot_temps = [temp for _ in range(20) if (temp := random.randrange(90, 110)) >= 100]
