import itertools


def range_diff(r1, r2):
    s1, e1 = r1
    s2, e2 = r2
    endpoints = sorted((s1, s2, e1, e2))
    result = []
    if endpoints[0] == s1 and endpoints[1] != s1:
        result.append((endpoints[0], endpoints[1]))
    if endpoints[3] == e1 and endpoints[2] != e1:
        result.append((endpoints[2], endpoints[3]))
    return result


def multi_range_diff(train_from_to, excluded):
    for from_to in excluded:
        train_from_to = list(itertools.chain(*[range_diff(date, from_to) for date in train_from_to]))
    return train_from_to


def multi_range_diff_simplified(train_from_to, excluded):
    for from_to in excluded:
        intervals = [range_diff(date, from_to) for date in train_from_to]
        train_from_to = [item for sublist in intervals for item in sublist]
    return train_from_to


if __name__ == '__main__':
    training_start_end = [(10, 100)]
    excluded_intervals = [(30, 40), (60, 80)]
    print(multi_range_diff_simplified(training_start_end, excluded_intervals))
